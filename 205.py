from itertools import product
wins = 0
for peter in product(range(1,5), repeat=9):
    if sum(peter) > 3.5*6:
            wins += 1
print(wins)
print(wins/(4**9))

