#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(input())

    bin_n = bin(n)

    count = 0
    max_count = 0
    
    for i in bin_n:
        if i == '1':
            count += 1
        else:
            count = 0

        if max_count < count:
            max_count = count

    print(max_count)