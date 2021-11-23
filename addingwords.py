worth = {}
while True:
    inputs = input()
    if inputs == "clear":
        break
    else:
        words = inputs.split()
        if words[0] == "def":
            worth[words[1]] = words[2]
        elif words[0] == "calc":
            words.pop(words[0])
            expression = ""
            i = 1
            for word in words:
                if i % 2 != 0:
                    if worth[word]:
                        expression = expression + worth[word]
                    else:
                        print("unknown")
                else:
                    expression = expression + word
            print(expression)

            