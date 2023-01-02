from random import randint
count = 0
rounds = 100_000
for round in range(rounds):
    seen = set()
    curr = 0
    while 1000 - curr not in seen:
        curr = randint(0, 999)
        seen.add(curr)
        count += 1
print(count / rounds)
