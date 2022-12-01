from imports import *
#================================================================
#
# Function: findNearest(arr, value):
#
# Description: This function takes is just used for finding the
#              nearest value in an array to the value input
#
# Returns: index of nearest value
#
#================================================================
def findNearest(arr, value):
    idx = (np.abs(arr - value)).argmin()
    return idx