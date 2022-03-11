for i in range(int(input())):
    statement = "what does the fox say?"
    words = input().split()
    to_del = []
    while True:
        command = input()
        if command == statement: 
            for word in words:
                if word not in to_del: print(word, end= " ")
            break
        command = command.split()
        to_del.append(command[2])