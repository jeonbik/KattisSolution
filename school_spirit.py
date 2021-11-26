# -*- coding: utf-8 -*-
"""School_spirit.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13rOLfOCgCHM9EvnI5lmm-FwsWWkz-R2t
"""

def scores(values):
  sum = 0
  for i in range(len(values)):
    sum += values[i] * ((4/5)**i)
  
  return sum/5
num = int(input())
inputs_ = []
for j in range(num):
   values = int(input())
   inputs_.append(values)
ans = scores(inputs_)
print(ans)

new_avg = 0
for k in range(num):
  new_array = inputs_.copy()
  del new_array[k]
  new_avg += scores(new_array)
print(new_avg/num)

