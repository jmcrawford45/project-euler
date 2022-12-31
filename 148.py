def pascal(n):
    def newrow(row):
        "Calculate a row of Pascal's triangle mod 7 given the previous one."
        prev = 0
        for x in row:
            yield (prev + x) % 7
            prev = x
        yield 1

    prevrow = [1]
    yield prevrow
    for _ in range(n):
        prevrow = list(newrow(prevrow))
        yield prevrow

def count_divisible_in_row(i) -> int:
    if i >= 7:
            triangles, per_triangle = divmod(i, 7)
            return triangles * (6-per_triangle)
    return 0

curr = 0
my_count = 0
for i, row in enumerate(pascal(52)):
    curr += len([c for c in row if c != 0])
    my_count += len(row) - count_divisible_in_row(i)
    print(i, curr)
    # assert my_count == curr



def count_not_divisible(rows) -> int:
    divisible = 0
    for i in range(rows):
        divisible += count_divisible_in_row(i)

    return rows*(rows+1)//2 - divisible
assert count_not_divisible(2) == 2*3//2
assert count_not_divisible(8) == 8*9//2-6
assert count_not_divisible(14) == 14*15//2-21
print(count_not_divisible(99))
# assert count_not_divisible(100) == 2361