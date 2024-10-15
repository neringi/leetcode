#!/bin/python3
# HackerRank Day 11: 2D arrays

import math
import os
import random
import re
import sys

if __name__ == '__main__':

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    # print(arr)

    sum_arr = []

    for i in range(0,4):
        for j in range (0,4):
            sum_arr.append(arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2])
            # print(sum_arr)

    print(max(sum_arr))

    