def is_prime(num):
    for i in range(2,num):
        if num %i==0:
            return False
            break 
        else:
            return True
def nth_print(num):
    initPrimeNum = 3
    init_prime_index = 2
    while (init_prime_index <= num):
        initPrimeNum += 2
        if (is_prime(initPrimeNum)):
            init_prime_index += 1
    return (initPrimeNum)
print(nth_print(6))