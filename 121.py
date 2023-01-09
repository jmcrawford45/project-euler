# TODO: we brute forced with sims, think about solving analytically
from random import randint
from math import floor
games = 50_000_000
rounds = 15
wins = 0
for game in range(games):
    discs = 0
    for round in range(rounds):
        if randint(1, round + 2) == 1:
            discs += 1
    if discs > rounds / 2:
        wins += 1
    if game and game % 100_000 == 0:
        print(f"probability of winning is {wins/game}")
        print(floor(game/wins)-1)
    