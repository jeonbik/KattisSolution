import sys
t = sys.stdin.readline().strip()
for i in range(int(t)):
    numbers = sys.stdin.readline().strip()
    num_store = []
    found = False
    for i in range(int(numbers)):
        num = sys.stdin.readline().strip()
        init_digits = ""
        for digits in num:
            init_digits+= digits
            if init_digits in num_store:
                found = True
        num_store.append(num)
    if found: print("NO")
    else:print("YES")


