from typing import Callable, Iterator, Optional, TypeVar

TItem = TypeVar('TItem')


def search(
        start: TItem,
        end: TItem,
        get_next: Callable[[TItem], Iterator[TItem]],
        get_distance: Callable[[TItem], int],
        max_depth: Optional[int] = None) -> Optional[list[TItem]]:
    """Do an A* search for `end` starting at `start`.

    Args:
        start (TItem): The starting point for the search.
        end (TItem): The end point for the search.
        get_next (Callable[[TItem], Iterator[TItem]]): A function that returns all items
            that can be reached from the given item.
        get_distance: (Callable[[TItem], int]): A function that returns a lower bound for
            the number of steps from the given item to `end`. The return value should be
            as high as possible but never higher than the actual number of steps.
        max_depth (Optional[int], optional): The maximum number of steps from `start` to `end`.
            If a path from `start` to `end` is known its, length should be supplied here.
            Defaults to None.

    Returns:
        Optional[list[TItem]]: A list with the steps from `start` to `end` or None.
    """
    if start == end:
        return [start]
    get_next(start)
