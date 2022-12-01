# Histogram-Equalization-and-Matching
This project takes in two images, and either applies histogram equalization to one image or applies histogram matching between the two images

## Notes
This project takes in either one image and applies histogram equalization, and then displays the newly equalized image, or it takes in two images and matches the histogram from the second image to the first image. Both situations utilize the tkinter image browser to display the results of the process.

## Usage:
<pre>
python sample.py -h -g -s sampling_method -d depth -i intensity -f imagefile
        -s : sampling method. 1 for pixel deletion/replication, 2 for pixel averaging/interpolation [default: 1]
        -d : Number of levels for downsampling [default: 1]
        -i : Intensity levels, between 1 and 7 [default: 1]  
        -f : Image input path
        -g : grayscale the input image [default: false]
