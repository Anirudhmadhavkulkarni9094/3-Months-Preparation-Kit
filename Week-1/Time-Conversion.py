#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    t = s[:8]                     #this line is used to take everything except the "AM" AND "PM" using splicing
    dn = s[8:]                    #this line is used to take only "AM" and "PM"
    h, m, s = t.split(':')
    h = int(h)
    if dn == "PM":
        if h != 12:
            h += 12
        return f"{h}:{m}:{s}"
    else:
        if h == 12:
            h = "0"
        h = "0" + str(h)
        return f"{h}:{m}:{s}"
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
