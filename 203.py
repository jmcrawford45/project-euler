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

from functools import lru_cache

@lru_cache(maxsize=None)
def is_squarefree(i) -> int:
    if i >= 7:
            triangles, per_triangle = divmod(i, 7)
            return triangles * (6-per_triangle)
    return 0

curr = 0
my_count = 0
for i, row in enumerate(pascal(51)):
    curr += len([c for c in row if c != 0])
    my_count += len(row) - count_divisible_in_row(i)
    print(i, curr)
    # assert my_count == curr