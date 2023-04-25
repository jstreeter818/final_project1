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
