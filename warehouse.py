num = int(input())
for i in range(num):
    stores = {}
    items = int(input())
    for j in range(items):
        items,val = input().split()
        val = int(val)
        if items in stores:
            amount = stores[items]
            val += amount
        stores[items] = val
    list_ = [v[0] for v in sorted(stores.items(), key=lambda kv: (-kv[1], kv[0]))]
    print(len(stores))
    for items in list_:
        print(items,stores[items])