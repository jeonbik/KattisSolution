# -*- coding: utf-8 -*-
"""Anthony and Diablo.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19BuLp9FHfnXYRMYLWad8R7tQYcf23rwY
"""

import math as m
A,N = map(float,input().split())
status = False
length =  N/(2*m.pi)

if m.pi * length * length >= A:
  print("Diablo is happy!")
else:
  print("Need more materials!")

