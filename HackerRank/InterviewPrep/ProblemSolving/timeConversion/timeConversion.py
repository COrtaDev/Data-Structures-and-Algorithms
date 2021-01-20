#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    # this will call for some string manipulation
    # we can separate hours, mins, and seconds
    hrs = s[0:2]
    mins = s[3:5]
    secs = s[6:8]
    # and lastly separate AM or PM
    meridian = s[8:10]
    # we can setup logic for edge cases 12 AM which is 00 mil time
    # and for 12 PM it is just 12 mil time
    if meridian == 'AM' and hrs == '12':
        hrs = '00'
        return hrs + ':' + mins + ':' + secs
    elif meridian == 'PM' and hrs == '12':
        return hrs + ':' + mins + ':' + secs
    elif meridian == 'PM' and hrs != '12':
        hrs = str(int(hrs) + 12)
        return hrs + ':' + mins + ':' + secs
    else:
        return hrs + ':' + mins + ':' + secs
    

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
