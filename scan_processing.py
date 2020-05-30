"""
This module is responsible for processing images
Tries to presrve color

History:
2020...... started development as a part of the scan_img project
2020.05.26 added comments
"""

import skimage
import numpy as np


def apply_filter(image, block_size=51, offset=0.07):
    """
    Process image
    :param image: ndarray, gray or rgb. This object is deleted
    :param block_size: parameter of skimage.filters.threshold_local, see https://scikit-image.org/docs/stable/api/skimage.filters.html#skimage.filters.threshold_local
    :param offset: parameter of skimage.filters.threshold_local, see https://scikit-image.org/docs/stable/api/skimage.filters.html#skimage.filters.threshold_local
    :return: processed image, same type as input image
    """
    # Convert to gray
    gr_image = skimage.color.rgb2gray(image)
    # Calculate threshold
    thresh = skimage.filters.threshold_local(gr_image, block_size, offset=offset)
    mask = gr_image < thresh
    # Apply mask
    sel = np.ones_like(image) * 255
    sel[mask] = image[mask]
    # Clear memory
    del gr_image
    del mask
    del image
    # Adjust gamma
    sel = skimage.exposure.adjust_gamma(sel, 1.3)
    return sel


def read_process_save(in_full_name, out_full_filename):
    # Lossless processing
    # This function is NOT used by default
    image = skimage.io.imread(in_full_name)
    processed = apply_filter(image)
    skimage.io.imsave(out_full_filename, processed)
    return


def read_process_save_A4(in_full_name, out_full_filename):
    """
    Read image, process it, and save.
    :param in_full_name: full name (path + filename) of the input image
    :param out_full_filename: full name (path + filename) of the output image
    :return: None
    """
    image = skimage.io.imread(in_full_name)
    # Scale images to fit A4 at some dpi
    resolution = (3508, 2480) # 300 dpi
    resized_image = skimage.transform.resize(image, resolution)
    del image
    resized_image = 255 * resized_image
    resized_image = resized_image.astype(np.uint8)
    # Go on to process
    processed = apply_filter(resized_image)
    # Save
    skimage.io.imsave(out_full_filename, processed)
    return
