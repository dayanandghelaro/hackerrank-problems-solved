#!/bin/python3

import sys
import math

def lowestTriangle(base, area):
    # Complete this function
    h = 2*area/base
    h = math.ceil(h)
    return h

base, area = input().strip().split(' ')
base, area = [int(base), int(area)]
height = lowestTriangle(base, area)
print(height)
