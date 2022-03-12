import sys
row,column,diagonal_1,diagonal_2 = set(),set(),set(),set()
for i in range(8):
    arrange = input().split()
    for character in arrange:
        if character == "*":
            row.add(i),column.add(arrange.index(character)),diagonal_1.add(i+arrange.index(character)),diagonal_2.add(i-arrange.index(character))
    if len(row) == 8 and len(column) == 8 and len(diagonal_1) == 8 and len(diagonal_2) == 8: print("valid")
    else: print('invalid') 



