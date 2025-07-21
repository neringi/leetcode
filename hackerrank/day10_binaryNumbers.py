#!/bin/python3
# HackerRank day 10

# For a given n, convert to base2 and count largest consecutive 1s

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    base2="{0:b}".format(n)
    # print('Base2: ', base2)
    maximum=0
    count=0
    for i in base2:
        # print(i)
        if i == '1':
            count += 1
        else:
            count = 0
        maximum = max(maximum,count)
        # print('Max: ', maximum)
    print(maximum)