import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#
# Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. Print the decimal value of each fraction on a new line with  places after the decimal.
# The first line contains an integer, n, the size of the array.
# The second line contains  space-separated integers that describe arr[n].


def plusMinus(arr):
    # print('Your array is: ', arr)
    positive = sum(1 for i in arr if i > 0)
    negative = sum(1 for i in arr if i < 0)
    zero = sum(1 for i in arr if i == 0)

    positive_ratio = round((positive / len(arr)), 6 )
    negative_ratio = round((negative / len(arr)), 6 )
    zero_ratio = round((zero / len(arr)), 6 )

    return print( f'{positive_ratio:.6f}'), print(f'{negative_ratio:.6f}'), print(f'{zero_ratio:.6f}')

            

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
