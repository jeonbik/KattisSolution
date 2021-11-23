
height,width,bricksnum = map(int,input().split())
brickslist = list(map(int,input().split()))
result = True
for i in range(height):
    sum = 0
    while sum < width and brickslist:
        sum +=  brickslist[0]
        brickslist.pop(0)
    if sum != width:
        result = False
        break
    
    elif not brickslist and i+1 != height:
        result = False

if result:
    print("YES")
else:
    print("NO")
