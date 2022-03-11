import re
while(True):
    try:
        to_find = input()
        if not to_find:break
        string = input()
        if len(to_find)>1 and len(set(to_find)) == 1 and len(set(string)) == 1: to_find = set(to_find)
        result = [m.start() for m in re.finditer(to_find,string)]
        for digits in result:print(digits,end= " ")
        print("\n")
    except:break