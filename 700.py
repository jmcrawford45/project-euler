accumulator = 1504170715041707
modulus = 4503599627370517
curr = 1504170715041707+accumulator % modulus
coins = set([1504170715041707])
while True:
    if curr < min(coins):
        print(curr)
        coins.add(curr)
    elif curr in coins:
        break
    curr += accumulator
    curr %= modulus

print(sum(coins))