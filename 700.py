accumulator = 3451657199285664
modulus = 4503599627370517
curr = 3451657199285664
coins = set([0])
while True:
    if curr > max(coins):
        print(curr)
        print(f"sum {sum(coins)}")
        coins.add(curr)
    elif curr in coins:
        break
    curr += accumulator
    curr %= modulus

print(sum(coins))