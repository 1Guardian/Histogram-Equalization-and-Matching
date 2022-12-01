from imports import *
from findNearest import *

#================================================================
#
# Function: histoMatching(referenceImage, image, imageOrHisto)
#
# Description: This function takes in a reference image and 
#              extracts the histogram from it. It then normalizes
#              the histogram and applies it to the given image.
#
# Returns: image | image that has had reference images' histogram 
#          applied
#
#================================================================

def histoMatching(referenceImage, image, imageOrHisto):

    #make numpy stop formatting for debugging
    np.set_printoptions(suppress=True)
    finalImage = np.copy(image)
    referenceHistogram = []
    referenceHistogramNormalized = []
    originalHistogram = []
    originalHistogramNormalized = []

    #determine if we were given an image or histo
    if (imageOrHisto):

        #variable to store the old histogram
        referenceHistogram = np.zeros([256])

        #get the pixel intensity value of each pixel
        for x in range(referenceImage.shape[0]):
            for y in range(referenceImage.shape[1]):
                referenceHistogram[int(referenceImage[x, y])] += 1

        #manipulating the histogram
        referenceHistogramNormalized = np.copy(referenceHistogram)

        #normalize the histogram
        for i in range(len(referenceHistogramNormalized)):
            referenceHistogramNormalized[i] = referenceHistogramNormalized[i]/sum(referenceHistogramNormalized)

        #get CDF
        for i in range(int(len(referenceHistogramNormalized)) - 1):

            if i > 0:
                referenceHistogramNormalized[i] = referenceHistogramNormalized[i-1] + referenceHistogramNormalized[i]

    else:

        #our histogram is the 'image'
        referenceHistogram = referenceImage
                
        #normalizedHistogram the histogram
        referenceHistogramNormalized = np.copy(referenceHistogram)

        #get CDF
        for i in range(int(len(referenceHistogramNormalized)) - 1):

            if i > 0:
                referenceHistogramNormalized[i] = referenceHistogramNormalized[i-1] + referenceHistogramNormalized[i]

    #now get the histogram and normalized histogram for the image we want to modify
    originalHistogram = np.zeros([256])

    #get the pixel intensity value of each pixel 
    for x in range(image.shape[0]):
        for y in range(image.shape[1]):
            originalHistogram[int(image[x, y])] += 1

    #manipulate the histogram
    originalHistogramNormalized = np.copy(originalHistogram)

    #normalize the histogram
    for i in range(len(originalHistogramNormalized)):
        originalHistogramNormalized[i] = originalHistogramNormalized[i]/sum(originalHistogramNormalized)

    #get CDF
    for i in range(int(len(originalHistogramNormalized)) - 1):

        if i > 0:
            originalHistogramNormalized[i] = originalHistogramNormalized[i-1] + originalHistogramNormalized[i]

    #now actually apply histogram matching by making the original image's histogram fit the new shape created by
    #the reference image's histogram
    for x in range(image.shape[0]):
        for y in range(image.shape[1]):
            newPixel = findNearest(referenceHistogramNormalized, originalHistogramNormalized[int(image[x, y])])
            image[x,y] = newPixel

    return image