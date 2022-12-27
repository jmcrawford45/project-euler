def gcd(x,y):
    while x != y:
        if x > y:
            x -= y
        else:
            y -= x
    return x

lcm = lambda x, y: x*y/gcd(x,y)

lcm_base = 1
for i in range(20):
    lcm_base = lcm(lcm_base, i+1)

print(lcm_base)
