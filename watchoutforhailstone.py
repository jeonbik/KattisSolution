# init_val = 0
val = int(input())
def recursive_fun(val):
    # global init_val
    if val == 1:
        return 1
    if val %2 == 0:
        val += recursive_fun(val//2)
        return val
    val += recursive_fun(3*val+1)
    return val
print(recursive_fun(val))
