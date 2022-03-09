import sys
for line in sys.stdin:
    line_ = list(map(int,line.split(" ")))
    sum_ = sum(line_)
    print(sum_//2)
