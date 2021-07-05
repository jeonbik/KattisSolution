itr = int(input())
input_str = []
for a in range(itr):
    string = input()
    input_str.append(string)
for b in range(len(input_str)):
    val = int((len(input_str[b]))**0.5)
    array = [[0 for k in range (val)] for l in range (val)]
    decrypt = []
    count = 0
    for i in range(val):
        for j in range(val):
            array[i][j] = input_str[b][val*i+j]      
    for m in range(val-1,-1,-1):
        for n in range(val):
            decrypt.append(array[n][m])
    print("".join(map(str,decrypt)))