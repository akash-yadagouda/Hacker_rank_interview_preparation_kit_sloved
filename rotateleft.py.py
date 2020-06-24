#!/bin/python3

import math
import os
import random
import re
import sys

def rotate(a,k,l):
    b=k
    temp=a
    p=l
    k=len(a)
    for i in range(k):
        if p<=k-1:
            temp[i]=a[p]
            p=p+1
        else:
            j=0
            while i<=k-1:
                temp[i]=b[j]
                j=j+1
                i=i+1
            break
    return temp



if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))
    b=a.copy()

    ans=rotate(a,b,d)
    for i in range(len(ans)):
        print(ans[i],end=" ")
