# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 11:53:09 2019

@author: Akash
"""

#!/bin/python3

import math
import os
import random
import re
import sys
import numpy as np

# Complete the hourglassSum function below.
def hourglassSum(arr):
    max1=0
    for k in range(4):
        for l in range(4):
            h=np.zeros([3,3],dtype=int)
            for i in range(3):
                for j in range(3):
#                    if i!=1 and j!=0:
#                        pass
#                    elif i!=1 and j!=2:
#                         pass
#                    else:
                    h[i][j]=arr[k+i][l+j]
                h[1][0]=0
                h[1][2]=0
                        
            su=np.sum(h)
            
#            print(h)
#            print(su)
            if su>=max1:
                max1=su
                
    return max1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
