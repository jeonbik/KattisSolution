# -*- coding: utf-8 -*-
"""ABC.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10hwJlZFDats7GBPzkNaPaXBlDn7r64yn
"""

from sys import stdin
values = list(map(int,input().split()))
values = sorted(values)
#a,b,c = map(int,stdin.readline().split())
format = input()
for letter in format:
  if letter == 'A':
    print(values[0],end=' ')
  elif letter =='C':
    print(values[2],end=' ')
  else:
    print(values[1],end=' ')



