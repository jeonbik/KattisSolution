lines = int(input())
sentences = []
b = "Simon says "
for k in range(lines):
    line = input()
    sentences.append(line)
c=[]
for j in range(len(sentences)):
    if sentences[j].startswith(b):
        d=sentences[j].replace(b,'')
        c.append(d)
for k in range(len(c)):
    print("".join(str(i) for i in c[k]))