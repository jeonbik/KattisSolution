num = int(input())
values = list(int(input()) for i in range(0,num))
for k in values:
    if(k%2==0):
        print(k," is even")
    else:
        print(k," is odd")
