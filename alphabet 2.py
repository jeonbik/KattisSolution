# -*- coding: utf-8 -*-
"""Alphabet.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hUNafyfCjyITRbVtpTl1hKEmlabRMw6z
"""

string = input()
n = len(string)
arr= list(string)
number = 1
arrayint = [0] * n
arrayint[0] = 1 
for i in range(1,n):
  arrayint[i] = 1
  for j in range(0,i):
    if arr[i] > arr[j] and arrayint[i] < (arrayint[j]+1):
      arrayint[i] = arrayint[j] + 1
      if arrayint[i] > number:
        number = arrayint[i]
print(26-number)