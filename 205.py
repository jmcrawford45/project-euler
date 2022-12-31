from random import randint
games = 10_000_000
res = 0
for i in range(games):
    if i % 1_000_000 == 0:
        print(res/(i+1))
    peter = sum(randint(1, 4) for _ in range(9))
    colin = sum(randint(1, 6) for _ in range(6))
    if peter > colin:
        res += 1
print(res/games)
