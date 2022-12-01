# Histogram-Equalization-and-Matching
This project takes in two images, and either applies histogram equalization to one image or applies histogram matching between the two images

## Notes
This project takes in either one image and applies histogram equalization, and then displays the newly equalized image, or it takes in two images and matches the histogram from the second image to the first image. Both situations utilize the tkinter image browser to display the results of the process. IT can also take a stored histogram (one file with 256 lines with probabilities on each) and match an input image with the histogram.

## Usage:
<pre>
python histo.py -h -m -i imagefile -r referencefile
        -m : 1 for histogram equalization, 2 for histogram matching via image, 3 for histogram matching via histogram file
        -g : Include to set any input images to grayscale for histogram manipulation
        -s : Take in image and save it's normalized histogram to a file
        imagefile : image file that you want to work on
        referencefile : reference image file for histogram matching, or a 256 line histogram file for matching
