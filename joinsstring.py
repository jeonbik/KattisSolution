import sys
dict_ = {}
num = int(input())+1
for i in range(1,num):
    dict_[i] = input()
print(dict_)
last = 0
for j in range(num-2):
    a,b = map(int,input().split())
    dict_[a] = dict_[a] + dict_[b]
    del(dict_[b])
for v in dict_.values():print(v)

