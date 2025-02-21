from altitude import max_altitude


def test_example_1():
    gain = [-5, 1, 5, 0, -7]
    assert max_altitude(gain) == 1


def test_example_2():
    gain = [-4, -3, -2, -1, 4, 3, 2]
    assert max_altitude(gain) == 0


def test_example_3():
    gain = [1, 2, 3, 4, 5]
    assert max_altitude(gain) == 15


def test_example_4():
    gain = [0, 0, 0, 0, 0]
    assert max_altitude(gain) == 0


def test_example_5():
    gain = [-1, -2, -3, -4, -5]
    assert max_altitude(gain) == 0
