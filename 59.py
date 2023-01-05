from collections import Counter
with open('cipher.txt') as f:
    codes = [int(c) for c in f.read().strip().split(",")]

key = []
key_len = 3
while len(key) < key_len:
    # most common english char is e
    key.append(Counter([c for i, c in enumerate(codes) if i % 3 == len(key)]).most_common(2)[1][0] ^ ord('e'))
out = ""
for i, c in enumerate(codes):
    out += chr(c ^ key[i % 3])
print(out)
print(len(out))
print(len(codes))
print(sum(ord(c) for c in out if c.isascii()))
