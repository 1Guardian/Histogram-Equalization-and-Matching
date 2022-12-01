from imports import *

#================================================================
#
# Function: grayScaleImage(image)
#
# Description: This function is just a wrapper for the open cv
#              grayscaling procedure since it has to be able to 
#              catch any opencv exceptions, and exception handling
#              in main makes it cluttered and hard to read.
#
# Returns: image | openCV image
#
#================================================================
def grayScaleImage(image):

    try:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    except Exception:
        print("Grayscale conversion failed. Perhaps the in path was empty or invalid. Exiting.")
        sys.exit(-1)

    return image