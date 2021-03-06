# -*- coding: utf-8 -*-
"""Cup_stacking.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13fMeAZTgoUC2DYo_ygEaGJGg90Cx-G2v
"""

num = int(input())
cup_dict = {}
for  i in range(num):
  a,b = input().split()
  try:
    if a.isdigit():
      radius = int(a)/2
      cup = b
      cup_dict[radius] = cup
    else:
      radius = int(b)
      cup = a
      cup_dict[radius] = cup
  except ValueError:
    pass
    
for key in sorted(cup_dict):
  print(cup_dict[key])