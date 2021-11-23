import sys
worth = {}
for inputs in sys.stdin:
    words = inputs.split()
    if len(words) == 1 and words[0] == "clear":
        worth.clear()
    elif words[0] == "def":
        worth[words[1]] = words[2]
    else:
        UnknownRaven = False
        expression = ''
        words.remove(words[0])
        i = 1
        for word in words:
            if word in ["+","-","="]:
                
                expression += word
            else:
                try:
                    expression += worth[word]
                except KeyError:
                    UnknownRaven = True
                    break                      
        if UnknownRaven:
            print(*words,"unknown")
        else: 
            expressionCopy = expression[:-1]
            value = eval(expressionCopy) 
            if str(value) not in worth.values():
                print(*words,"unknown")
            else:
                print(*words,list(worth.keys())[list(worth.values()).index(str(value))])
