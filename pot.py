# -*- coding: utf-8 -*-
"""pot.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ssgAtFTCO3Gwa8LQlSzTxIgoEJ0UqJPV
"""

val = int(input())
sum = 0
for i in range(val):
  numbers = input()
  number = str(0)
  power = 0
  for i in range(0,len(numbers)):
    if i<(len(numbers)-1):
      number += str(numbers[i])
    else:
      power = int(numbers[i])
  sum += int(number) **power

print(sum)