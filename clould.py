# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 21:11:04 2019

@author: Akash
"""


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    jump=0
    current_pos=0
    while current_pos!=len(c)-1:
        if c[current_pos+1]==0:
            if current_pos+1==len(c)-1:
                jump=jump+1
                current_pos=current_pos+1
                if current_pos==len(c)-1:
                    break
            if c[current_pos+2]==0:
                jump=jump+1
                current_pos=current_pos+2
                if current_pos==len(c)-1:
                    break
            elif c[current_pos+2]==1:
                jump=jump+1
                current_pos=current_pos+1
                if current_pos==len(c)-1:
                    break
                
                
        else:
            if c[current_pos+2]==0:
                jump=jump+1
                current_pos=current_pos+2
                if current_pos==len(c)-1:
                    break
            else:
                print("stop")
                break
    print(jump)
    
    return jump
            
                
                
        
 
        
            

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    #fptr.write(str(result) + '\n')

    #fptr.close()
