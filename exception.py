#!/bin/python3

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