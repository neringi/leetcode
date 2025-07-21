#!/bin/python3

# HackerRank Day 16

# Read a string, S, and print its integer value; 
# if S cannot be converted to an integer, print Bad String.

import math
import os
import random
import re
import sys



S = input()

try:
    num = int(S)
    print(num)
except ValueError:
    print("Bad String")