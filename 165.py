from functools import lru_cache
from fractions import Fraction

@lru_cache(maxsize=None)
def s(n):
    if n == 0:
        return 290797
    else:
        return pow(s(n-1), 2, 50515093)

def t(n):
    return s(n) % 500
segments = []
from dataclasses import dataclass
@dataclass
class Point:
    x: int
    y: int

    def __hash__(self):
        return hash((self.x, self.y))
@dataclass
class Segment:
    start: Point
    end: Point
    @property
    def m(self):
        if self.end.x - self.start.x != 0:
            return Fraction(self.end.y - self.start.y, self.end.x - self.start.x)

    @property
    def b(self):
        slope = self.m
        if slope == 0:
            return self.end.y
        return self.end.y - (slope * self.end.x)  # type: ignore

    def vertical_intersect(self, other):
        m2 = other.m
        b2 = other.b
        y_intercept = m2 * self.start.x + b2
        if other.start.x < self.start.x < other.end.x and min(self.start.y, self.end.y) < y_intercept < max(self.start.y, self.end.y):
            return Point(self.start.x, y_intercept)


    def interior_intersect(self, other) -> Point | None:
        # m1*x + b1 = m2*x + b2
        # x(m1-m2) = b2-b1
        # x = (b2-b1)/(m1-m2)
        if self.end.x - self.start.x == 0 and other.end.x - other.start.x == 0:
            return None
        elif self.end.x - self.start.x == 0:
            return self.vertical_intersect(other)
        elif other.end.x - other.start.x == 0:
            return other.vertical_intersect(self)
        else:
            m1 = self.m
            m2 = other.m
            if m1 == m2:
                return None
            b1 = self.b
            b2 = other.b
            x_intercept = Fraction(b2-b1, m1-m2)
            if self.start.x < x_intercept < self.end.x and other.start.x < x_intercept < other.end.x:
                return Point(x_intercept, m1*x_intercept+b1)
# given
l1 = Segment(Point(12, 32), Point(27, 44))
l2 = Segment(Point(17, 62), Point(46, 53))
l3 = Segment(Point(22, 40), Point(46, 70))
# mine
flat = Segment(Point(0,0), Point(5,0))
vertical = Segment(Point(2, -1), Point(2, 1))
one_slope = Segment(Point(-10,-10), Point(10,10))
negative_one_slope = Segment(Point(-10,10), Point(10,-10))
small_one_slope = Segment(Point(0,1), Point(1,2))
assert not small_one_slope.interior_intersect(one_slope)
assert not small_one_slope.interior_intersect(negative_one_slope)
assert one_slope.interior_intersect(negative_one_slope) == Point(0,0)
assert not flat.interior_intersect(flat)
assert not flat.interior_intersect(Segment(Point(0,1), Point(5,1)))
assert not flat.interior_intersect(Segment(Point(1,0), Point(6,0)))
assert not vertical.interior_intersect(vertical)
assert not vertical.interior_intersect(Segment(Point(2, 1), Point(2, 3)))
assert flat.interior_intersect(vertical) == Point(2, 0)
assert l1.m == Fraction(12, 15)
assert l2.m == Fraction(-9, 29)
assert l1.b == 32-Fraction(96, 10)
assert l2.interior_intersect(l3)
assert not l3.interior_intersect(l1)
assert not l1.interior_intersect(l2)

for i in range(0, 5000):
    p1 = t(i*4+1), t(i*4+2)
    p2 = t(i*4+3), t(i*4+4)
    if p1 < p2:
        segments.append(Segment(Point(*p1), Point(*p2)))
    else:
        segments.append(Segment(Point(*p2), Point(*p1)))
assert segments[0] == Segment(Point(12, 232), Point(27, 144))
assert len(segments) == 5000
res = set()
for i, segment in enumerate(segments):
    if i % 50 == 0:
        print(f"{i/50}%")
    for segment2 in segments[i+1:]:
        intersect = segment.interior_intersect(segment2)
        if intersect is not None and intersect not in [segment.start, segment.end, segment2.start, segment2.end]:
            res.add(intersect)
print(len(res))
