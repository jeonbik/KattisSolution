num = int(input())
arr = []
for i in range(num):
    val = int(input())
    arr.append(val)
for k in range(len(arr)):
    print(arr[(len(arr)-1)-k])