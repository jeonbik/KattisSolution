import sys
x1,y1 = map(int,sys.stdin.readline().split())
x2,y2 = map(int,sys.stdin.readline().split())
x3,y3 = map(int,sys.stdin.readline().split())
if x1==x2: x4 = x3
elif x2==x3: x4 = x1
else: x4 = x2
if y1==y2:y4=y3
elif y2==y3: y4 = y1
else: y4 = y2
sys.stdout.write(str(x4)+ " "+str(y4)+"\n")

x1,y1 = map(int,input().split())
x2,y2 = map(int,input().split())
x3,y3 = map(int,input().split())
if x1==x2: x4 = x3
elif x2==x3: x4 = x1
else: x4 = x2
if y1==y2:y4=y3
elif y2==y3: y4 = y1
else: y4 = y2
print(x4,y4)