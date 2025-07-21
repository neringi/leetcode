#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'flippingBits' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#
# The first line of the input contains q, the number of queries.
# Each of the next q lines contain an integer, n, to process.

def flippingBits(n):
    bit32='{:032b}'.format(n)
    # print(bit32)
    invert=''

    for i in bit32:
        if i == '0':
            invert += '1'
        else:
            invert += '0'

    return int(invert, 2)

    # print(n)
    # for query in n:
    #     print(query)
    #     string = str(query)
    #     print(string)
        # for i in string:
        #     print(i)

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        result = flippingBits(n)
        print(result)

    #     fptr.write(str(result) + '\n')

    # fptr.close()
