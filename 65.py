from fractions import Fraction
approximation = [2, 1, 2]
while len(approximation) < 100:
    if (1+len(approximation)) % 3 == 0:
        approximation.append(2*(1+len(approximation)) // 3)
    else:
        approximation.append(1)
print(approximation)
accumulator = None
for i in reversed(approximation):
    if accumulator is None:
        accumulator = i
    else:
        accumulator = Fraction(1, accumulator) + i
print(sum(int(c) for c in str(accumulator.numerator)))
