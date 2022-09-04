import pytest
from typing import Iterator
from a_star import search


class Graph:
    def __init__(self, graph: dict[str, tuple[int, list[str]]]):
        self.graph = graph

    def get_min_distance(self, item: str) -> int:
        return self.graph[item][0]

    def get_next(self, item: str) -> Iterator[str]:
        return iter(self.graph[item][1])


def test_search_with_cycle():
    assert search(1, 2, lambda _: [1], lambda _: 3) is None


def test_search_with_max_length():
    assert search(1, 2, lambda _: [2], lambda _: 3, 2) is None


@pytest.mark.parametrize("graph,path", (
    (Graph({
        "A": (0, [])
    }), ["A"]),
    (Graph({
        "A": (1, ["B"]),
        "B": (0, [])
    }), ["A", "B"]),
    (Graph({
        "A": (1, ["B", "D"]),
        "B": (1, ["C"]),
        "C": (1, ["E"]),
        "D": (2, ["E"]),
        "E": (1, ["F"]),
        "F": (0, [])
    }), ["A", "D", "E", "F"])
))
def test_search_graph(graph, path):
    assert search(path[0], path[-1], graph.get_next, graph.get_min_distance) == path
