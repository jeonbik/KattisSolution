# -*- coding: utf-8 -*-
"""Reversed binary Numbers.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hXKvA66oR4RhAUsne07jwoWFDaF9QSx2
"""

num = int(input())
binary = bin(num)
binary = binary[2:]
binary = binary[::-1]
print(int(binary,2))

