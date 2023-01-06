denominations = {
    "I": 1,
    "IV": 4,
    "V": 5,
    "IX": 9,
    "X": 10,
    "XL": 40,
    "L": 50,
    "XC": 90,
    "C": 100,
    "CD": 400,
    "D": 500,
    "CM": 900,
    "M": 1000
}

to_numeral = {v: k for k, v in denominations.items()}

def parse(numeral: str) -> int:
    res = 0
    i = 0 
    while i < len(numeral):
        c = numeral[i]
        if c in "IXC" and i < len(numeral) - 1 and denominations[c] < denominations[numeral[i+1]]:
            # check for substractive
            res += -denominations[c] + denominations[numeral[i+1]]
            i += 2
        else:
            res += denominations[c]
            i += 1
    return res

def minimize(x: int) -> str:
    out = ""
    for val in sorted(to_numeral, reverse=True):
        out += to_numeral[val] * (x // val)
        x %= val
    return out
        
    

assert parse("MCCCCCCVI") == 1606
assert parse("XIX") == 19

res = 0
with open('roman.txt') as f:
    for line in f.read().strip().splitlines():
        line = line.strip()
        res += len(line) - len(minimize(parse(line)))
print(res)
