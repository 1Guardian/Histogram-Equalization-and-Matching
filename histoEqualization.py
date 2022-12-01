from imports import *

#================================================================
#
# Function: histoEqualization(image, extension, path, name)
#
# Description: This function applies histogram equalization to an 
#              image, implemented from scratch. If the algorithm
#              needs to be modified in the final version when I
#              actually take the class, it should not be difficult
#
# Returns: image | image that has had histogram equalization applied
#
#================================================================
def histoEqualization(image):

    #global values for use in process
    finalImage = np.copy(image)
    originalHistogram = np.zeros([256])
    equalizedHistogram = np.zeros([256])
    originalHistogramPMF = np.zeros([256])
    originalHistogramCDF = np.zeros([256])

    #get the pixel intensity value of each pixel
    for x in range(image.shape[0]):
        for y in range(image.shape[1]):
            originalHistogram[int(image[x, y])] += 1

    #get PMF of pixel counts
    for i in range(len(originalHistogram)):
        originalHistogramPMF[i] = originalHistogram[i]/sum(originalHistogram)

    #get CDF from PMF
    for i in range(len(originalHistogramPMF)):
        if (i == 0):
            originalHistogramCDF[i] = originalHistogramPMF[i]
        else:
            originalHistogramCDF[i] = originalHistogramCDF[i-1]+originalHistogramPMF[i]

    #multiply each CDF value by number of bits-1 (256) for our images
    for i in range(len(originalHistogramCDF)):
        equalizedHistogram[i] = int(originalHistogramCDF[i] * 255)

    #apply the histogram back onto the image
    for x in range(image.shape[0]):
        for y in range(image.shape[1]):
            finalImage[x, y] = equalizedHistogram[int(image[x, y])]

    return finalImage