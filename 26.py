def long_division_cycle(numerator: int, denominator: int) -> str:
    """Can't use builtin div because rounding errors. Don't return cycle"""
    out = ""
    seen = dict()
    while True:
        numerator *= 10
        if numerator == 0:
            return ""
        elif (numerator, denominator) in seen:
            return out[seen[(numerator, denominator)]:]
        seen[(numerator, denominator)] = len(out)
        while numerator < denominator:
            numerator *= 10
            out += "0"
        next_digit, numerator = divmod(numerator, denominator)
        out += str(next_digit)

print(1+max(len(long_division_cycle(1, i)) for i in range(1, 1000)))

