#!/bin/python3

import math
import os
import random
import re
import sys

# HackerRank
# 
# Given a square matrix, calculate the absolute difference between the sums of its diagonals.
# 
# Completed the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#
# Input: The first line contains a single integer, n, the number of rows and columns in the square matrix arr.
# Each of the next n lines describes a row, arr[i], and consists of n space-separated integers arr[i][j].

def diagonalDifference(arr):
    diagonal = sum([arr[i][i] for i in range(len(arr))])
    diagonal2 = sum([row[-i-1] for i,row in enumerate(arr)])
    diff = abs(diagonal - diagonal2)
    return diff

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    # fptr.write(str(result) + '\n')

    # fptr.close()
