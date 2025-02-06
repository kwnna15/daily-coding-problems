from maxarea import max_area


def test_example_1():
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    assert max_area(height) == 49


def test_example_2():
    height = [1, 1]
    assert max_area(height) == 1


def test_example_3():
    height = [4, 3, 2, 1, 4]
    assert max_area(height) == 16


def test_example_4():
    height = [1, 2, 1]
    assert max_area(height) == 2


def test_example_5():
    height = [2, 3, 4, 5, 18, 17, 6]
    assert max_area(height) == 17
