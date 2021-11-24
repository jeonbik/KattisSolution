num = int(input())
input_arr = []
for i in range(num):
    a,b = map(int,input().split())
    input_arr.append((a,b))
for j in range(len(input_arr)):
    print(input_arr[j][0]," ",int(input_arr[j][1]+(input_arr[j][1]*(input_arr[j][1]+1)/2)))