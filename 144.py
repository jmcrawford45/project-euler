from dataclasses import dataclass
from math import *
from fractions import Fraction
@dataclass
class Point:
    x: float
    y: float

@dataclass
class Line:
    slope: float
    intercept: float
def compute_intersect(line: Line, start: Point) -> Point:
    """sub for y=mx+b before squaring to expand"""
    slope, intercept = line.slope, line.intercept
    a = 4+slope**2
    b = 2*slope*intercept
    c = intercept**2 - 100
    x_solutions = ((-b + sqrt(b**2 - 4*a*c)) / (2*a)), ((-b - sqrt(b**2-4*a*c)) / (2*a))
    y_solutions = (sqrt(100-4*x_solutions[0]**2)), (sqrt(100-4*x_solutions[1]**2))
    if abs(x_solutions[0]-start.x) > abs(x_solutions[1]-start.x):
        return Point(x_solutions[0], slope*x_solutions[0]+intercept)
    return Point(x_solutions[1], slope*x_solutions[1]+intercept)

def normal(point: Point) -> Line:
    slope = -4 * point.x / point.y
    intercept = point.y - slope * point.x
    return Line(slope, intercept)

def reflect(start: Line, reflection: Line, point: Point) -> Line:
    slope = tan(2*atan(reflection.slope) - atan(start.slope))
    intercept = point.y - slope * point.x
    return Line(slope, intercept)



assert compute_intersect(Line(-19.7/1.4, 10.1), Point(0, 10.1)) == Point(1.4, -9.6)
assert reflect(Line(-19.7/1.4, 10.1), normal(Point(1.4, -9.6)), Point(1.4, -9.6)).slope == -0.6631933513819811

line = Line(-19.7/1.4, 10.1)
intercept = Point(0, 10.1)
hits = 0
while hits < 1000:
    # if hits > 10:
    #     break
    # print(intercept, line, hits)
    intercept = compute_intersect(line, intercept)
    if -0.01 < intercept.x < 0.01:
        print(hits, abs(intercept.x))
    line = reflect(line, normal(intercept), intercept)
    hits += 1
print(hits)



