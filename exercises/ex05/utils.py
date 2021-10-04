"""List utility functions part 2."""

__author__ = "730320843"

# Define your functions below


def only_evens(xs: list[int]):
    """Return even ints from a list."""
    if len(xs) == 0:
        return []
    evens = []
    for x in xs:
        if x % 2 == 0:
            evens.append(x)
    return evens


def sub(xs: list[int], start: int, end: int):
    """Create subset list."""
    if len(xs) == 0 or start > len(xs) or end <= 0 or start >= end:
        return []
    if start < 0:
        start = 0
    if end > len(xs):
        end = len(xs)
    counter = start
    sublist = []
    while counter < end:
        sublist.append(xs[counter])
        counter += 1
    return sublist


def concat(xs: list[int], ys: list[int]):
    """Concat some lists."""
    if len(xs) == 0:
        return ys
    if len(ys) == 0:
        return xs
    new_list = []
    for x in xs:
        new_list.append(x)
    for y in ys:
        new_list.append(y)
    return new_list