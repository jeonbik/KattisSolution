k, m,n = map(int,input().split())
div = k // (m+n)
used = div * (m+n)
rem = k - used
if rem >= m: print("Alex")
else: print("Barb")

