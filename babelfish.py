import sys
dict_ ={}
for line in sys.stdin:
    line_ = line.split()
    if len(line_) == 2: dict_[line_[1]] = line_[0]
    elif len(line_) == 1:
        if line_[0] in dict_:print(dict_[line_[0]])
        else:print("eh")