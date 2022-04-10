#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#
def breakingRecords(scores):
    most, least = scores[0], scores[0]                        #this is used to set minimum score in order to compare
    countmax, countmin = 0, 0
    for i in scores:
        if i > most:
            most = i
            countmax += 1
        if i < least:
            least = i
            countmin += 1
            
    return [countmax, countmin]
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
