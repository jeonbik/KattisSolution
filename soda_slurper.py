# -*- coding: utf-8 -*-
"""Soda_Slurper.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12tqcZJcnJW79U3AI92gFRtGcuxp4mn3J
"""

e,f,c = map(int,input().split())
initial = e+f
count = 0
while(initial >=c):
  initial -=c
  count +=1
  initial +=1
print(int(count))

