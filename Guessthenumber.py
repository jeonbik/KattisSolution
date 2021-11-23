low = 1
high = 1000
avg = int((low + high) / 2)
print(avg)
while True:
    response = input()
    if response== "higher":
        low = avg
        avg = int((low + high + 1) / 2)
    if response== "lower":
        high = avg
        avg = int((low + high) / 2)

    if response== "correct":
        break
    print(avg)

