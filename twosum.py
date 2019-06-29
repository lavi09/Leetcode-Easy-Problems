# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 17:13:01 2019

@author: Lavi
"""

"""Naive Solution
def twosum(a,target):
    n=len(a)
    i=0
    j=1
    total=0
    for i in range(0,n):
    
        
        for j in range(i+1,n):
            total=a[i]+a[j]
            if total==target :
                print(i,j)
                break
"""
"""Faster Solution"""

def twosum(nums,target):
    d={}
    for i,num in enumerate(nums):
        n=target-num
        if n not in d:
            d[num]=i
        else:
            print([d[n],i])
            
        
        



a=[2,7,11,15]
target=9
twosum(a,target)