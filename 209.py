res = 0
for i in range(0, 2**7):
    a,b,c,d,e,f = [i & (2**p) for p in range(6)]
    b
    res += 1
print(res)