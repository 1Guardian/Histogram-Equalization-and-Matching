from imports import *

#================================================================
#
# Function: getMetaData(image, imagePath, type, outPath)
#
# Description: This function gets the metadata of the passed
#              image file. MetaData collected includes: name
#              path, image file type, image size, number of 
#              pixels, and image file size
#
# Returns: metaData | type: dictionary of metadata
#
#================================================================
def getMetaData(image, imagePath, imgType, outPath):

    #dict of metadata for image
    metaData = dict()

    #add name to dict
    metaData.update({"name": os.path.basename(imagePath)})

    #add path to dict
    metaData.update({"path": outPath + '/' + os.path.basename(imagePath) + imgType})

    #add file extension to dict
    metaData.update({"ext": imgType})

    #get image size (x and y)
    y, x, a = image.shape 
    metaData.update({"sizeX": x})
    metaData.update({"sizeY": y})

    #get image size (total pixels)
    metaData.update({"pixelCt": x*y})

    #get image size (bytes)
    metaData.update({"byteSize": os.stat(imagePath).st_size})

    #get the image creation date (this corresponds to when I got the image)
    metaData.update({"obtained": str(datetime.fromtimestamp(os.stat(imagePath).st_ctime))})

    return metaData
