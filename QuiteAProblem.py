import sys
for sentence in sys.stdin:
    temp = sentence.split()
    a = list(map(lambda x: x.lower(), temp))
    if any('problem' in s for s in a):
        print("yes")
    else:
        print("no")