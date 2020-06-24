# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 22:26:32 2019

@author: Akash
"""


import math
import os
import random
import re
import sys
def cal_req_pos(number,req_pos):
    req_pos.clear()
    for i in range(len(number)):
        req_pos.append(number[i]-1)
        print("req_pos",req_pos)
# Complete the minimumBribes function below.
def minimumBribes(a):
   
    numbers=[]
    real_pos=[]
    Bribes=[]
    
    for i in range(len(a)):
        if a[i]!=i+1:
            numbers.append(a[i])
            real_pos.append(i+1)
            
    print("real_pos",real_pos)        
            
    print(numbers)
    req_pos=[]
    
    for i,j in zip(real_pos,req_pos):
        if abs(i-j)>2:
            print("too chotic")
            return
    for i,j in zip(real_pos,req_pos):
        if abs(i-j)==1:
            print(i,j)
            
#            a[i-1]=numbers[j-1]
            
            
        
            
    
    for i in range(len(numbers)):
        index=int(req_pos[i-1])-1
        num=int(numbers[i])
        a[index]=num
        cal_req_pos(numbers,req_pos)
#        a.insert(req_pos[i]-1,numbers[i])
            
        
        
        
    return a
        
        
            
    
    
    
    

if __name__ == '__main__':
    q=[1,2,3,4,5,8,6,7]
    
#    q[0]=q[3]
#    print(q)
    print(minimumBribes(q))
    
 
    
