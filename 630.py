from functools import lru_cache
from fractions import Fraction

@lru_cache(maxsize=None)
def s(n):
    if n == 0:
        return 290797
    else:
        return pow(s(n-1), 2, 50515093)

def t(n):
    return (s(n) % 2000) - 1000
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
            return Fraction(self.end.y - self.start.y,self.end.x - self.start.x)

    @property
    def b(self):
        slope = self.m
        if slope == 0:
            return self.end.y
        if slope is None:
            return self.end.x
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

points = []
for k in range(1, 2501):
    p1 = t(k*2-1), t(k*2)
    points.append(Point(*p1))
assert points[:3] == [Point(527, 144), Point(-488, 732), Point(-454, -947)]

def l(points, n):
    segments = {}
    for i, p1 in enumerate(points[:n]):
        for p2 in points[:n][i+1:]:
            if p1.x > p2.x:
                s = Segment(p2, p1)
            else:
                s = Segment(p1, p2)
            segments[(s.m, s.b)] = s
    return segments.values()
assert len(l(points, 3)) == 3
assert len(l(points, 100)) == 4948
from collections import Counter
lines = l(points, 100)
assert sum(v[1] * (len(lines)-v[1]) for v in Counter([s.m for s in lines]).most_common()) == 24477690
lines = l(points, 2500)

print(sum(v[1] * (len(lines)-v[1]) for v in Counter([s.m for s in lines]).most_common()))


