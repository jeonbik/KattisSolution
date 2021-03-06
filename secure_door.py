# -*- coding: utf-8 -*-
"""secure_door.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17hcupdzpN11S__JiWPLsBzPhqaRDtu8z
"""

data_array = []
while(True):
  try:
    action, name = input().split()
  except EOFError:
    break
  if action =="entry" and name in data_array:
    print("{} {} {}".format(name,"entered","(ANOMALY)"))
  elif action == "exit" and name not in data_array:
    print("{} {} {}".format(name,"exited","(ANOMALY)"))
  elif action == "entry":
    print("{} {}".format(name,"entered"))
    data_array.append(name)
  else:
    print("{} {}".format(name,"exited"))
    k = data_array.index(name)
    data_array.pop(k)