from typing import Iterator
from a_star import search


def test_search_returns_start_if_equal_to_end():
    assert search(1, 1, lambda _: [], lambda _: 0) == [1]


def test_search_with_two_steps():
    assert search(1, 2, lambda _: [2], lambda _: 3) == [1, 2]


def test_search_with_cycle():
    assert search(1, 2, lambda _: [1], lambda _: 3) is None


def test_search_with_max_length():
    assert search(1, 2, lambda _: [2], lambda _: 3, 2) is None


def test_search_with_initial_wrong_path():
    assert search(
        1,
        9,
        lambda i: [3, 8] if i == 2 else [i + 1],
        lambda i: i
    ) == [1, 2, 8, 9]


def test_search_graph():
    graph = Graph({
        "A": (1, ["B", "D"]),
        "B": (1, ["C"]),
        "C": (1, ["E"]),
        "D": (2, ["E"]),
        "E": (1, ["F"]),
        "F": (0, [])
    })
    assert search("A", "F", graph.get_next, graph.get_min_distance) == ["A", "D", "E", "F"]


class Graph:
    def __init__(self, graph: dict[str, tuple[int, list[str]]]):
        self.graph = graph

    def get_min_distance(self, item: str) -> int:
        return self.graph[item][0]

    def get_next(self, item: str) -> Iterator[str]:
        return iter(self.graph[item][1])
