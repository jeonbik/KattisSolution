participants = int(input())
values = {}
value = list(map(int,input().split()))
minimum = min(value)
for digit in value:
    if digit in values:
        values[digit] = values[digit]+1
    else:
        values[digit] = 1
    
key = sorted(values.keys(),reverse=True)
found = False
for k in key:
    if values[k] == 1:
        print(value.index(k)+1)
        found = True
        break
if not found:
    print("none")


    