# -*- coding: utf-8 -*-
"""Odd Man Out.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jH0wflCcRRfgviQCh16dQUOT7e11R9NX
"""

num = int(input())
for i in range(num):
  num = int(input())
  val = list(map(int,input().split()))
  val_set = set(val)
  for v in val_set:
    ct = val.count(v)
    if ct == 1:
      print('{} {}{}{} {}'.format("Case","#",i+1,":",v))
      break

