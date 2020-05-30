# Scanned/photographed document processing

This package is intendend for processing poor quality images of some documents on white paper (lecture notes, etc.).
It processes images (attempting to preserve pen colour) and assemples a .pdf file.  
This program does not use the `OpenCV` package.


#### Usage

*Where to put raw images:*
the directory `img_raw` contains subdirectories, each subdirectory contains images (no other files allowed).
The program then assembles a separate .pdf file for each subdirectory.


1. Put your images in subdirectories (or in a single subdirectory) inside the `img_raw` folder
2. Run `go_over_folders.py` 
3. Collect your .pdf's from the folder `pdf`.

In this version, the folder `img_raw` already contains some sample images.
To test the program, simply run `go_over_folders.py`.
Or simply see the results in the folders `img_processed` and `pdf`.


#### Additional notes

The algorythm applies a threshold filter and rescales images to fit exactly the A4 format at 300 dpi.   
During the rendering, the program will print our the progress status and estimated time left.

Parameters `block_size` and `offset` in the function
`scan.apply_filter(..)` were found ad-hoc. They might be changed, if necessary.

This module requires the package `img2pdf` (for information see e.g. [here](https://pypi.org/project/img2pdf/); installing on Anaconda guide [here](https://anaconda.org/conda-forge/img2pdf)).
It also uses `skimage`.

You should ignore the warnings `UserWarning: ... is a low contrast image`, if they ever come up.

#### History 

- early 2020  started development  
- 2020.05.26  added comments  
- 2020.05.28  extensively tested with Anaconda-3.7