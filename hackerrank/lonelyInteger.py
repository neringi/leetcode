#!/bin/python3

import math
import os
import random
import re
import sys

# HackerRank
# 
# Given an array of integers, where all elements but one occur twice, find the unique element.
#
# Completed the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#
# Input: The first line contains a single integer, n, the number of integers in the array.
# The second line contains n space-separated integers that describe the values in a.

def lonelyinteger(a):
    for i in a:
        if a.count(i) == 1 :
            return i

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
