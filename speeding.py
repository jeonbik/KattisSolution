# -*- coding: utf-8 -*-
"""Speeding.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18EvaA-CYA5GRQh23w0pV--cxje1tNMYf
"""

num  = int(input())
for  i in range(num):
  t,d = map(int,input().split())
  if i == 1:
    prev_time = t
    prev_dist = d
    speed = d/t
  if i>1:
    new_speed = (d - prev_dist)/(t-prev_time)
    if new_speed > speed:
      speed = new_speed
    prev_dist = d
    prev_time = t

print(int(speed))

