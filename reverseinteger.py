# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 19:12:34 2019

@author: Lavi
"""




def reverseint(a):
    flag=False
    if a <0:
        a=-a
        flag=True

    total=0    
    while(a!=0):
        d=a%10
        total=total*10+d
        a=a//10
    if total > pow(2,31) or total< pow (-2,31) :
        print(0)
    if flag:
        print(-total)
    else:
        print(total)



a=1534236469
reverseint(a)







