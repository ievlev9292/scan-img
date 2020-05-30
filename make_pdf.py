"""
This module is responsible for compiling .pdf
from prepared images

History:
2020.05... started development as a part of the scan_img project
2020.05.26 added comments
"""

import img2pdf  ## See https://pypi.org/project/img2pdf/
import os


def compile_pdf_from_img(img_dir, output_pdf_filename):
    """
    Compile and save .pdf from images
    :param img_dir: path to directory with images
    :param output_pdf_filename: full name (path + filename) of the output .pdf
    :return: None
    """
    # Get list of images filenames
    imagelist = [os.path.join(img_dir, f) for f in os.listdir(img_dir) if os.path.isfile(os.path.join(img_dir, f))]
    # Specify paper size (A4)
    a4inpt = (img2pdf.mm_to_pt(210),img2pdf.mm_to_pt(297))
    layout_fun = img2pdf.get_layout_fun(a4inpt)
    # Make and save .pdf
    with open(output_pdf_filename, "wb") as f:
        f.write(img2pdf.convert(imagelist, layout_fun=layout_fun))
    return
