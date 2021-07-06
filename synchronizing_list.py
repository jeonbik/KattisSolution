main_array = []

while True:
    num = int(input())
    if num ==0:
        break
    else:
        data_array_1 = list(int(input()) for i in range(0,num))
        data_arra_2 = list(int (input()) for i in range(0,num))
        main_array.append((data_array_1,data_arra_2))

def print_data(list_1,list_2):
  index_array= []
  list_3 = sorted(list_1)
  list_4 = sorted(list_2)
  for a in list_1:
    k = list_3.index(a)
    index_array.append(k)
  for b in index_array:
    print(list_4[b])
    
for k in range(len(main_array)):
  print_data(main_array[k][0],main_array[k][1])
  print("\n")