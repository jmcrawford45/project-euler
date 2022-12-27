# known triplet with sum divisible by 1000 TODO: how to derive without brute forcing
triplet = (8,15,17)
scaler = 1000 // sum(triplet)
res = 1
for x in triplet:
    res *= x * scaler
print(res)