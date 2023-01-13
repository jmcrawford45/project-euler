from utils import primes_in_range

from dataclasses import dataclass

@dataclass
class Number:
    top: int
    top_left: int
    top_right: int
    middle: int
    bottom_left: int
    bottom_right: int
    bottom: int


    def __iter__(self):
        return (self.top, self.top_left, self.top_right, self.middle, self.bottom_left, self.bottom_right, self.bottom)

    def sum(self):
        return sum(self.__iter__())
    
    def diff(self, other: "Number") -> int:
        return sum([int(s1 != s2) for s1, s2 in zip(self.__iter__(), other.__iter__())])

numbers = {
    0: Number(1, 1, 1, 0, 1, 1, 1),
    1: Number(0, 0, 1, 0, 0, 1, 0),
    2: Number(1, 0, 1, 1, 1, 0, 1),
    3: Number(1, 0, 1, 1, 0, 1, 1),
    4: Number(0, 1, 1, 1, 0, 1, 0),
    5: Number(1, 1, 0, 1, 0, 1, 1),
    6: Number(1, 1, 0, 1, 1, 1, 1),
    7: Number(1, 1, 1, 0, 0, 1, 0),
    8: Number(1, 1, 1, 1, 1, 1, 1),
    9: Number(1, 1, 1, 1, 0, 1, 1),
}

def segments(num: int) -> int:
    return sum(numbers[int(c)].sum() for c in str(num))


def sam_count(nums: list[int]) -> int:
    return sum(2*segments(num) for num in nums)

def max_count(nums: list[int]) -> int:
    res = segments(nums[0]) + segments(nums[-1])
    prev = nums[0]
    for num in nums[1:]:
        # turn off / on non-overlap, then compute overlap
        to_trim = len(str(prev)) - len(str(num))
        if to_trim:
            res += segments(int(str(prev)[:to_trim]))
        for c1, c2 in zip(str(prev)[to_trim:], str(num)):
            res += numbers[int(c1)].diff(numbers[int(c2)])
        prev = num

    return res

def root_seq(num: int) -> list[int]:
    curr = num
    res = [num]
    while curr > 9:
        curr = sum(int(c) for c in str(curr))
        res.append(curr)
    return res
assert root_seq(137) == [137, 11, 2]
assert sam_count([137, 11, 2]) == 40
assert max_count([137, 11, 2]) == 30
assert sam_count(root_seq(1999993)) == 116
assert max_count(root_seq(1999993)) == 78

max_res = sam_res = 0
primes = primes_in_range(10**7, 2*10**7)
for p in primes:
    seq = root_seq(p)
    max_res +=  max_count(seq)
    sam_res += sam_count(seq)
print(sam_res - max_res)