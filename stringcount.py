# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 20:47:17 2019

@author: Akash
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    count=0
    k=len(s)
    u=int(n/k)
    for i in range(len(s)):
        if s[i]=='a':
            count=count+1
    kk=count
    kkk=kk*u
    left=n-(u*len(s))
    
    for h in range(left):
        if s[h]=='a':
            kkk=kkk+1
    return kkk
            
    

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())
    

    result = repeatedString(s, n)

    #fptr.write(str(result) + '\n')

#    fptr.close()
