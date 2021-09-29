"""List utility functions."""

__author__ = "730320843"


def all(xs: list[int], check: int) -> bool:
    """Do all the ints match?"""
    if len(xs) == 0:
        return False
    for x in xs:
        if x != check:
            return False
    return True


def is_equal(xs: list[int], ys: list[int]) -> bool:
    """Do list ints equate?"""
    if len(xs) != len(ys):
        return False

    i = 0
    while i < len(xs):
        if xs[i] != ys[i]:
            return False

        i += 1
    return True


def max(xs: list[int]) -> int:
    """Return max val of lists."""
    if len(xs) == 0:
        raise ValueError("max() arg is an empty List")
    maxx = xs[0]
    i = 0
    while i < len(xs):
        if maxx < xs[i]:
            maxx = xs[i]
        i += 1
    return maxx