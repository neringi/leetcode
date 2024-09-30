#!/bin/python3

import math
import os
import random
import re
import sys

# HackerRank 
#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#
# Input format: A single string s that represents a time in -hour clock format (i.e.: hh:mm:ssAM or hh:mm:ss:PM ).
# 
# Had to comment out HackerRank code to test since they have their output_path defined 

def timeConversion(s):
    if s[-2:] == "AM":
        if s[:2] == "12":
            return print("00" + s[2:-2])
        else:
            return print(s[:-2])
    elif s[-2:] == "PM":
        if s[:2] == "12":
            return print(s[:-2])
        else:
            return print(str(int(s[:2]) + 12) + s[2:-2])
     

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    # fptr.write(result + '\n')

    # fptr.close()
