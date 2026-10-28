import math

_a, _b, _c = 7, 2, 8
def triangle_perimeter(a=_a, b=_b, c=_c):
    return a + b + c
def triangle_area(a=_a, b=_b, c=_c):
    p = (a + b + c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))