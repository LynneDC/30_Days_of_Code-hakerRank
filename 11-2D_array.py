#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    if len(arr) < 6 or any(len(row) != 6 for row in arr):
        print("Input matrix must be 6x6")
    else:
        max_hourglass_sum = float('-inf')  # Initialize with negative infinity

        for i in range(4):
            for j in range(4):
                hourglass_sum = (
                    arr[i][j] + arr[i][j+1] + arr[i][j+2] +
                    arr[i+1][j+1] +
                    arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
                )
                max_hourglass_sum = max(max_hourglass_sum, hourglass_sum)

        print(max_hourglass_sum)
