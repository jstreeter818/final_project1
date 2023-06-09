import math


def circle(value):
    radius = float(value)
    if radius <= 0:
        raise TypeError
    return math.pi * radius ** 2


def square(value):
    side = float(value)
    if side <= 0:
        raise TypeError
    return side * side


def rectangle(value1, value2):
    length, width = float(value1), float(value2)
    if length <= 0 or width <= 0:
        raise TypeError
    return length * width


def triangle(value1, value2):
    base, height = float(value1), float(value2)
    if base <= 0 or height <= 0:
        raise TypeError
    return (1 / 2) * base * height


def trapezoid(value1, value2, value3):
    base, base2, height = float(value1), float(value2), float(value3)
    if base <= 0 or height <= 0 or base2 <= 0:
        raise TypeError
    return (base2 + base) / 2 * height


def rhombus(value1, value2):
    width, height = float(value1), float(value2)
    if width <= 0 or height <= 0:
        raise TypeError
    return (1 / 2) * width * height


def ellipse(value1, value2):
    axis1, axis2 = float(value1), float(value2)
    if axis1 <= 0 or axis2 <= 0:
        raise TypeError
    return math.pi * axis1 * axis2
