"""Unit tests for list utility functions."""

# TODO: Uncomment the below line when ready to write unit tests
from exercises.ex05.utils import only_evens, sub, concat

__author__ = "730320843"


def test_evens_empty() -> None:
    """Test empty list."""
    assert only_evens([]) == []


def test_evens_list() -> None:
    """Test use case one."""
    xs: list[int] = [1, 2, 3, 4]
    assert only_evens(xs) == [2, 4]


def test_evens_all_evens() -> None:
    """Test all evens."""
    xs: list[int] = [2, 4, 6, 8]
    assert only_evens(xs) == [2, 4, 6, 8]


def test_sub_negative_start() -> None:
    """Test negative start index."""
    xs: list[int] = [2, 4, 6, 8]
    assert sub(xs, -2, 3) == [2, 4, 6]


def test_sub_small() -> None:
    """Test small sublist."""
    xs: list[int] = [2, 4, 6, 8]
    assert sub(xs, 1, 2) == [4]


def test_sub_large() -> None:
    """Test larger sublist."""
    xs: list[int] = [2, 4, 6, 8, 10, 12]
    assert sub(xs, 1, 4) == [4, 6, 8]


def test_concat_empty() -> None:
    """Test empty concat."""
    xs: list[int] = [1, 2, 3, 4]
    assert concat(xs, []) == [1, 2, 3, 4]


def test_concat_small() -> None:
    """Test small concat."""
    xs: list[int] = [1, 2]
    ys: list[int] = [3, 4]
    assert concat(xs, ys) == [1, 2, 3, 4]


def test_concat_large() -> None:
    """Test large concat."""
    xs: list[int] = [1, 2, 3, 4]
    ys: list[int] = [5, 6, 7]
    assert concat(xs, ys) == [1, 2, 3, 4, 5, 6, 7]
