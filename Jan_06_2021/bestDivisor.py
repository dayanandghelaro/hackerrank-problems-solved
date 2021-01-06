#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    if 1 <= n <= 10**5:
        fptr = open(os.environ['OUTPUT_PATH'], 'w')
        maxS = 0
        divisor = 1
        for i in range(1, n+1):
            if n%i == 0:
                s = sum([int(d) for d in str(i)])
                if s > maxS:
                    maxS = s
                    divisor = i
        fptr.write(str(divisor))
        fptr.close()
