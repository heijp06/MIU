import pytest
from a_star import search
from typing import Iterator, TypeVar

TItem = TypeVar('TItem')


def test_search_returns_start_if_equal_to_end():
    assert search(1, 1, fail_get_next, fail_get_distance) == [1]


def fail_get_next(item: TItem) -> Iterator[TItem]:
    raise AssertionError(f"get_next({item}) was called.")


def fail_get_distance(item: TItem) -> int:
    raise AssertionError(f"get_distance({item}) was called.")
