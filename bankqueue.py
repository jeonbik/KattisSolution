total_person,total_minutes = map(int,input().split())
holdings = {}
for i in range(total_person):
    moeny,time = map(int,input().split())
    if time in holdings: holdings[time].append(moeny)
    else: holdings[time] = [moeny]
total_money = 0
collection = []
for t in range(total_minutes,-1,-1):
    if t in holdings:
        money = holdings[t]
        for m in money: collection.append(m)
        if collection:
            total_money += max(collection)
            collection.remove(max(collection))
print(total_money)
