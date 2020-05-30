"""
This module puts all parts together into one assemply line:
import, process and save images --> compile and save .pdf --> report back

History:
2020...... Started development as a part of the scan_img project
2020.05.26 Added comments
2020.05.29 Extensively tested
"""

import os
from scan_processing import read_process_save_A4
from make_pdf import compile_pdf_from_img
import utils as utils

# Adjustable constants
START_TIME = utils.time.time() # to count total spent time
IMG_RAW_DIR = 'img_raw' # This directory contains further subdirectories (a.k.a. 'page sets') with images
IMG_PROCESSED_DIR = 'img_processed' # The directory where processed images will be put
if not os.path.exists(IMG_PROCESSED_DIR):
    os.makedirs(IMG_PROCESSED_DIR)
PDF_DIR = 'pdf' # The directory where the final .pdf's will be put
if not os.path.exists(PDF_DIR):
    os.makedirs(PDF_DIR)


# Get list of subdirectories in IMG_RAW_DIR
page_sets = [ f.path for f in os.scandir(IMG_RAW_DIR) if f.is_dir() ]
# Calculate total number of images to process
tot_iter = 0
for page_set in page_sets:
    list_of_files = [os.path.join(page_set, f) for f in os.listdir(page_set) if os.path.isfile(os.path.join(page_set, f))]
    tot_iter += len(list_of_files)
print(f'Discovered {len(page_sets)} sets of pages, total of {tot_iter} images')
# Go over each subdirectory (= page set)
page_set_counter = 0
current_iter = 0
start_time = utils.time.time()
for page_set in page_sets:
    # page_set is the current image directory path
    page_set_counter += 1
    print(f'Working with images in {os.path.basename(page_set)}, that is set {page_set_counter} out of {len(page_sets)} ...')
    # go over the filenames and prepare out-folder
    list_of_files = [os.path.join(page_set, f) for f in os.listdir(page_set) if os.path.isfile(os.path.join(page_set, f))]
    out_dir = os.path.join(IMG_PROCESSED_DIR, os.path.basename(page_set))
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)
    # Process images
    prefix = f'  |-- {os.path.basename(page_set)} (set {page_set_counter} of {len(page_sets)}) | Total : '
    for img_full_name in list_of_files:
        # Display counter
        utils.report_progress_time_simple(current_iter, tot_iter, start_time, prefix=prefix)
        current_iter += 1
        # Do the image
        out_full_filename = os.path.join(out_dir, os.path.basename(img_full_name))
        read_process_save_A4(img_full_name, out_full_filename)
    # Make .pdf
    print('Making .pdf ...')
    output_pdf_filename = os.path.join(PDF_DIR, os.path.basename(page_set) + '.pdf')
    compile_pdf_from_img(out_dir, output_pdf_filename)


### REPORT HOW MUCH TIME WAS SPENT
print()
print('All done!')
END_TIME = utils.time.time()
ELAPSED_SECONDS = END_TIME - START_TIME
ELAPSED_HOURS = ELAPSED_SECONDS / 3600
print("---- Elapsed time {:.2f} seconds, or {:.1f} hours ----".format(ELAPSED_SECONDS, ELAPSED_HOURS))
