# -*- coding: utf-8 -*-
"""Digit_product.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cLIIwo1GiPL9MarVh3R8fnKxuhBz6m3y
"""

import sys
num = sys.stdin.readline()
product = 11
while (product >=10):
  product = 1
  for digit in num:
    if int(digit) !=0:
      product *= int(digit)
  num = str(product)
print(product)