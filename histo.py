#==============================================================================
#
# Class : CS 5420
#
# Author : Tyler Martin
#
# Project Name : Project 4 | Applying Histogram Equalization to Images
#
# Date: 10-25-2022
#
# Description: This project works with histogram manipulation in three main
#              ways, first by applying histogram equalization to a target
#              image, second by applying histogram matching on a target
#              image from a reference image, and third applying a histogram 
#              to a target image from a file containing the histogram in a 
#              text file with eahc line representing an normalized intensity level 
#
# Notes: Since I know you prefer to read and work in C++, this file is set
#        up to mimic a standard C/C++ flow style, including a __main__()
#        declaration for ease of viewing. Also, while semi-colons are not 
#        required in python, they can be placed at the end of lines anyway, 
#        usually to denote a specific thing. In my case, they denote globals, 
#        and global access, just to once again make it easier to parse my code
#        and see what it is doing and accessing.
#
#==============================================================================

#"header" file imports
from imports import *
from checkImages import *
from getMetaData import *
from histoEqualization import *
from grayScaleImage import *
from saveImage import *
from hisogramMatching import *
from findNearest import *


#================================================================
#
# Function: __main__
#
# Description: This function is the python equivalent to a main
#              function in C/C++ (added just for ease of your
#              reading, it has no practical purpose)
#
#================================================================

def __main__(argv):

    #variables that contain the command line switch
    #information
    inPath = "nothing"
    refPath = "nothing"
    mode = 1
    grayscale = False
    saveHistogram = False

    # get arguments and parse
    try:
      opts, args = getopt.getopt(argv,"h:m:i:r:gs")

    except getopt.GetoptError:
        print("histo.py -h -m -i imagefile -r referencefile")
        print("===========================================================================================================")
        print("-m : 1 for histogram equalization, 2 for histogram matching via image, 3 for histogram matching via histogram file")
        print("-g : Include to set any input images to grayscale for histogram manipulation")
        print("-s : Take in image and save it's normalized histogram to a file")
        print("imagefile : image file that you want to work on")
        print("referencefile : reference image file for histogram matching, or a 256 line histogram file for matching")  
        sys.exit(2)

    for opt, arg in opts:

        if opt == ("-h"):
            print("histo.py -h -m -i imagefile -r referencefile")
            print("===========================================================================================================")
            print("-m : 1 for histogram equalization, 2 for histogram matching via image, 3 for histogram matching via histogram file")
            print("-g : Include to set any input images to grayscale for histogram manipulation")
            print("-s : Take in image and save it's normalized histogram to a file")
            print("imagefile : image file that you want to work on")
            print("referencefile : reference image file for histogram matching, or a 256 line histogram file for matching") 
            sys.exit(2)

        elif opt == ("-m"):
            if (int(arg) < 4 and int(arg) > 0):
                mode = int(arg)
            else:
                print("Invalid mode supplied. Valid modes are 1 - 3")

        elif opt in ("-i", "--indir"):
            
            #make sure path is a real file
            if os.path.isfile(arg):
                inPath = arg
            else:
                print("File passed for target image is not a real file. Please check to make sure the desired file exists.")
                sys.exit(-1)

        elif opt == ("-r"):

            #make sure reference file is a real file
            if os.path.isfile(arg):
                refPath = arg
            else:
                print("File passed for reference image is not a real file. Please check to make sure the desired file exists.")
                sys.exit(-1)

        elif opt == ("-g"):
            grayscale = True

        elif opt == ("-s"):
            saveHistogram = True

    #see if the program was invoked just to save a histogram
    if saveHistogram:
        saveImage(checkImages((len(checkImages(False, inPath).shape) == 3), inPath), "rawHistogram")
        sys.exit(2)

    #make sure we got at the least, a path
    if (inPath == "nothing"):
        print("you must provide a file to start with!")
        sys.exit(2)

    #if grayscale conversion not specified and color image passed, throw an error
    if (not grayscale and len(checkImages(False, inPath).shape) == 3):
        print("Color images are not allowed!")
        sys.exit(2)

    #make sure we got at the least, a path if the mode implies need of reference path
    if (refPath == "nothing" and mode > 1):
        print("you must provide a reference file to start with!")
        sys.exit(2)

    #if grayscale conversion not specified and color image passed, throw an error
    if (refPath != "nothing" and mode == 2):
        if (not grayscale and len(checkImages(False, refPath).shape) == 3):
            print("Color images are not allowed as reference images!")
            sys.exit(2)
        
    #fetch images and start function calls as specified by mode
    if (mode == 1):

        #Apply histogram Equalization 
        cv2.imshow("Original Image", checkImages(grayscale and (len(checkImages(False, inPath).shape) == 3), inPath))
        cv2.waitKey(0)
        cv2.imshow("Image With histogram equalization", histoEqualization(checkImages(grayscale and (len(checkImages(False, inPath).shape) == 3), inPath)))
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    elif (mode == 2):

        #apply histogram matching via image
        cv2.imshow("Original Image", checkImages(grayscale and (len(checkImages(False, inPath).shape) == 3), inPath))
        cv2.waitKey(0)
        cv2.imshow("Reference Image", checkImages(grayscale and (len(checkImages(False, refPath).shape) == 3), refPath))
        cv2.waitKey(0)
        cv2.imshow("Image With Matching Histogram", histoMatching(checkImages(grayscale and (len(checkImages(False, refPath).shape) == 3), refPath), checkImages(grayscale and (len(checkImages(False, inPath).shape) == 3), inPath), True))
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    elif (mode == 3):

        #apply histogram matching via histo file
        cv2.imshow("Original Image", checkImages(grayscale and (len(checkImages(False, inPath).shape) == 3), inPath))
        cv2.waitKey(0)
        cv2.imshow("Image With Matching Histogram File", histoMatching(loadtxt(refPath, comments="#", delimiter="\n", unpack=False), checkImages(grayscale and (len(checkImages(False, inPath).shape) == 3), inPath), False))
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    else:
        print("I don't know how we got here, but it's time to exit")
        sys.exit(2)

#start main
argv = ""
__main__(sys.argv[1:])