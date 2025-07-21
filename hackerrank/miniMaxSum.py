#!/bin/python3

import math
import os
import random
import re
import sys

# HackerRank 
#
# Completed the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#
# Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.
# 
# A single line of five space-separated integers.


def miniMaxSum(arr):
    arr.sort()
    # print('sorted array: ', arr)
    min = sum(arr[0:4])
    max = sum(arr[1:5])

    return print(min, max)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
