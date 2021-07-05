def sum(n):
    sum = 0
    for digit in (str(n)):
        sum += int(digit)
    return sum
def product(n,prev_sum):
    k = 11
    new_sum = sum(n*k)
    while(new_sum != prev_sum):
        k+=1
        new_sum = sum(n*k)    
    return(k)

in_put = 1
input_arr = []
while (in_put != 0):
    inputs = int(input())
    if inputs <= 0 or inputs >=100000:
        in_put = 0
    else:
        input_arr.append(inputs)
for i in range(len(input_arr)):
    val = product(input_arr[i],sum(input_arr[i]))
    print(val)

