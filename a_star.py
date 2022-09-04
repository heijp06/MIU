from __future__ import annotations
from typing import Callable, Iterator, Optional, TypeVar
from heapq import heappop, heappush

TItem = TypeVar('TItem')


def search(
        start: TItem,
        end: TItem,
        get_next: Callable[[TItem], Iterator[TItem]],
        get_min_distance: Callable[[TItem], int],
        max_length: Optional[int] = None) -> Optional[list[TItem]]:
    """Find the shortest path from `start` to `end`.

    Args:
        start (TItem): The starting point for the search.
        end (TItem): The end point for the search.
        get_next (Callable[[TItem], Iterator[TItem]]): A function that returns all items
            that can be reached from the given item.
        get_min_distance: (Callable[[TItem], int]): A function that returns a lower bound for
            the number of steps from the given item to `end`. The return value should be
            as high as possible but never higher than the actual number of steps.
        max_length (Optional[int], optional): The maximum number of steps from `start` to `end`.
            If an upper bound for the length of the path from `start` to `end` is known, it
            should be supplied here. Defaults to None.

    Returns:
        Optional[list[TItem]]: A list with the steps from `start` to `end` or None.
    """
    searcher = Searcher(start, end, get_next, get_min_distance, max_length)

    return searcher.search()


class Searcher:
    def __init__(
            self,
            start: TItem,
            end: TItem,
            get_next: Callable[[TItem], Iterator[TItem]],
            get_min_distance: Callable[[TItem], int],
            max_length: Optional[int]) -> None:
        self.start = start
        self.end = end
        self.get_next = get_next
        self.get_min_distance = get_min_distance
        self.max_length = max_length
        self.seen = set()
        self.heap = []
        self.result: Node = None

    def search(self) -> Optional[list[TItem]]:
        self.add_item(self.start, 0, None)

        while self.heap:
            min_distance, step, node = heappop(self.heap)
            if self.too_long(min_distance):
                break
            if node.item in self.seen:
                continue
            if node.item == self.end:
                self.max_length = step
                self.result = node
                continue
            self.seen.add(node.item)
            for next_item in self.get_next(node.item):
                self.add_item(next_item, step + 1, node)

        if self.result:
            return self.result.to_list()

        return None

    def add_item(self, item: TItem, step: int, parent: Optional[Node]) -> None:
        min_distance = step + self.get_min_distance(item)
        if self.too_long(min_distance):
            return
        heappush(self.heap, (min_distance, step, Node(item, parent)))

    def too_long(self, length: int) -> bool:
        if self.max_length is None:
            return False
        return length > self.max_length or self.result and length == self.max_length


class Node:
    def __init__(self, item: TItem, previous: Optional[Node]):
        self.item = item
        self.previous = previous

    def __repr__(self) -> str:
        return repr((self.item, self.to_list()))

    def to_list(self) -> list[TItem]:
        if self.previous:
            return self.previous.to_list() + [self.item]
        else:
            return [self.item]
