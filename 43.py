from itertools import permutations
def is_special(n: int) -> bool:
    if len(str(n)) != 10:
        return False
    return all([
        int(str(n)[1:4]) % 2 == 0,
        int(str(n)[2:5]) % 3 == 0,
        int(str(n)[3:6]) % 5 == 0,
        int(str(n)[4:7]) % 7 == 0,
        int(str(n)[5:8]) % 11 == 0,
        int(str(n)[6:9]) % 13 == 0,
        int(str(n)[7:10]) % 17 == 0,
    ])
sum_special = 0
for n in permutations([str(c) for c in range(10)]):
    x = int(''.join(n))
    try:
        if is_special(x):
            sum_special += x
    except:
        print(x)
print(sum_special)
