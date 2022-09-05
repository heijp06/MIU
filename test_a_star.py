import pytest
from typing import Iterator
from a_star import search


class Graph:
    def __init__(self, graph: dict[str, tuple[int, list[str]]]):
        self.graph = graph
        self.set_start_and_end()

    def set_start_and_end(self):
        starts = set(self.graph.keys())
        ends = set(
            node
            for _, nodes in self.graph.values()
            for node in nodes
        )
        start = starts - ends
        assert len(start) == 1, "No single start point."
        (self.start,) = start
        self.end = next(
            key
            for key, (_, value)
            in self.graph.items()
            if not value
        )

    def get_min_distance(self, item: str) -> int:
        return self.graph[item][0]

    def get_next(self, item: str) -> Iterator[str]:
        return iter(self.graph[item][1])


def test_search_with_max_length():
    assert search(1, 2, lambda _: [2], lambda _: 3, 2) is None


@pytest.mark.parametrize("graph,path,max_length", (
    (Graph({
        "A": (0, [])
    }), ["A"], None),
    (Graph({
        "A": (1, ["B"]),
        "B": (1, ["C"]),
        "C": (0, [])
    }), None, 1),
    (Graph({
        "A": (1, ["B"]),
        "B": (0, [])
    }), ["A", "B"], None),
    (Graph({
        "A": (1, ["B", "D"]),
        "B": (1, ["C"]),
        "C": (1, ["E"]),
        "D": (2, ["E"]),
        "E": (1, ["F"]),
        "F": (0, [])
    }), ["A", "D", "E", "F"], None)
))
def test_search_graph(graph, path, max_length):
    assert search(graph.start, graph.end, graph.get_next,
                  graph.get_min_distance, max_length) == path
