# -*- coding: utf-8 -*-
"""Convex_Polynomial.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zmDB4Ltmh3JBY0hZlDi94nWhaRRJZ73V
"""

num = int(input())
for i in range(0,num):
  array_x = []
  array_y = []
  list_ = list(map(int,input().split()))
  for i in range(1,len(list_)):
    if i%2!=0:
      array_x.append(list_[i])
    else:
      array_y.append(list_[i])
  array_x.append(array_x[0])
  array_y.append(array_y[0])
  first_term = 0
  second_term = 0
  ans = 0
  for i in range(0,len(array_x)-1):
    first_term += array_x[i]*array_y[i+1]
    second_term += array_y[i]*array_x[i+1]
  ans = (first_term - second_term)/2
  print(ans)