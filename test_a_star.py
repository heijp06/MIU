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
