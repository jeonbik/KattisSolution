# -*- coding: utf-8 -*-
"""Map_tiles.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11IjHzzd6OVxwHrIYq33zUzTD499ON673
"""

num = input()
level = len(num)
x= 0
y = 0
for i in range(level):
  if (int(num[i])==1 or int(num[i]) ==3):
    x += 2**(level -(i+1))

  if (int(num[i]) ==2 or int(num[i]) ==3):
    y += 2**(level-(i+1))

print(level,x,y)