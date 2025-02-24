from grid import equal_pairs


def test_example_1():
    grid = [[3, 2, 1], [1, 7, 6], [2, 7, 7]]
    assert equal_pairs(grid) == 1


def test_example_2():
    grid = [[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]]
    assert equal_pairs(grid) == 3


def test_example_3():
    grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    assert equal_pairs(grid) == 0


def test_example_4():
    grid = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    assert equal_pairs(grid) == 9


def test_example_5():
    grid = [[1, 2], [2, 1]]
    assert equal_pairs(grid) == 2
