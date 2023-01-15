accumulator = 1504170715041707
modulus = 4503599627370517
curr = 1504170715041707
coins = set([1504170715041707])
i = 1
while True:
    curr += accumulator
    curr %= modulus
    i += 1
    if curr < min(coins):
        print(curr, i)
        print(f"sum {sum(coins)}")
        coins.add(curr)
    elif curr in coins:
        break

print(sum(coins))