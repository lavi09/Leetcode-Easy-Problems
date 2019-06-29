# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 19:12:37 2019

@author: Lavi
"""

def integerpalindrome(a):
    total=0
    if a <0:
        print("false")
        
    while(a>total):        
        total=total*10+a%10
        a=a//10
    if (total==a or total//10==a):
        print("True")
    else:
        print("False")
        
    
    
    
    
    
num=12321
integerpalindrome(num)