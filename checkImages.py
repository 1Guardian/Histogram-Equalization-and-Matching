from imports import *
from grayScaleImage import *

#================================================================
#
# Function: checkImages(path)
#
# Description: This function takes in the image Path supplied to
#              it and returns the image read in, or a boolean
#              with the value 'False' if the read fails
#
# Returns: image | type: opencv image
#           OR
#          image | type: Boolean, Value: False
#
#================================================================
def checkImages(grayscale, path):

    #return object
    image = False

    #image types that we recognize
    valid_images = [".jpg",".gif",".png", ".jpeg"]

    #if file ends in a file extension associated with an image, we take it
    if os.path.splitext(path)[1].lower() in valid_images:

        try:
            if grayscale: 
                image = grayScaleImage(cv2.imread(path, cv2.IMREAD_UNCHANGED)) 
            else:
                image = cv2.imread(path, cv2.IMREAD_UNCHANGED) 
        except Exception:
            print("Reading image failed. Perhaps the in path was empty or invalid. Exiting.")
            sys.exit(-1)

    #return image or boolean
    return image 