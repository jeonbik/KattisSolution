# -*- coding: utf-8 -*-
"""prelides.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NYuG_syVM8n78cixPzwcG-axTsl9yJjj
"""

itr = 0
array_1 = ['A#','C#','D#','F#','G#']
array_2 = ['Bb','Db','Eb','Gb','Ab']
while True:
  try:
    values = list(input().split())
    itr +=1
    if (len(values)==0):
      break
    elif (len(values[0])==1):
      print('{} {}{} {}'.format('Case',itr,':','UNIQUE'))
    else:
      if values[0] in array_1:
        idx = array_1.index(values[0])
        print('{} {}{} {} {}'.format('Case',itr,':',array_2[idx],values[1]))
      else:
        idx = array_2.index(values[0])
        print('{} {}{} {} {}'.format('Case',itr,':',array_1[idx],values[1]))
  except EOFError:
    break

