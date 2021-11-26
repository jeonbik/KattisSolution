num = int(input())
data = list((input(),input()) for i in range(0,num))
for k in data:
    print(k[0])
    print(k[1])
    for i in range(len(k[0])):
        if k[0][i]==k[1][i]:
            print(".",end="")
        else:
            print('*',end="")
    print("\n")
