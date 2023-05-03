import math


def circle(value):
    radius = float(value)
    if radius <= 0:
        raise TypeError
    else:
        return 2 * math.pi * radius


def square(value):
    side = float(value)
    if side <= 0:
        raise TypeError
    else:
        return side * 4


def rectangle(value1, value2):
    side1, side2 = float(value1), float(value2)
    if side1 <= 0 or side2 <= 0:
        raise TypeError
    else:
        return (side1 * 2) + (side2 * 2)


def triangle(value1, value2, value3):
    base, side1, side2 = float(value1), float(value2), float(value3)
    if base <= 0 or side1 <= 0 or side2 <= 0:
        raise TypeError
    else:
        return base + side1 + side2


def trapezoid(value1, value2, value3, value4):
    base1, base2, side1, side2 = float(value1), float(value2), float(value3), float(value4)
    if base1 <= 0 or base2 <= 0 or side1 <= 0 or side2 <= 0:
        raise TypeError
    else:
        return base1 + base2 + side1 + side2


def rhombus(value):
    side = float(value)
    if side <= 0:
        raise TypeError
    else:
        return side * 4


def ellipse(value1, value2):
    axis1, axis2 = float(value1), float(value2)
    if axis1 <= 0 or axis2 <= 0:
        raise TypeError
    else:
        return 2 * math.pi * ((3 * axis1) + (2 * axis2) - (math.sqrt(axis1 * axis2)))
