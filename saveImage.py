from imports import *

#================================================================
#
# Function: saveImage(image, extension, path, name)
#
# Description: This function saves a given image as a normalized
#              histogram in a file for use with later parts of the
#              project
#
# Returns: boolean | true on success, false on failure
#
#================================================================
def saveImage(image, name):

    #get histogram
    normalizedHistogram = np.zeros(256)

    #variable to store the old histogram
    referenceHistogram = np.zeros([256])

    #get the pixel intensity value of each pixel
    for x in range(image.shape[0]):
        for y in range(image.shape[1]):
            referenceHistogram[int(image[x, y])] += 1

    #manipulate the histogram just like we would in the 
    #matching function
    normalizedHistogram = np.copy(referenceHistogram)

    #normalize the histogram
    for i in range(len(normalizedHistogram)):
        normalizedHistogram[i] = normalizedHistogram[i]/sum(normalizedHistogram)

    #write out histogram to file
    form="%s \n"
    with open(name,'w') as f:
        for i in range(len(normalizedHistogram)):
            f.write(form % (normalizedHistogram[i]))