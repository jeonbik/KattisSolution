# -*- coding: utf-8 -*-
"""phd_candidate.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rJ4tO4YGgCo14Ky1Qu7hcEPdL24ErZiw
"""

num = int(input())
for k in range(num):
  inputs_ = input()
  if inputs_ =="P=NP":
    print("skipped")
  else:
    list_ = inputs_.split('+')
    a = int(list_[0])
    b = int(list_[1])
    print(a+b)

22
a=['1','2','3','4','5']

