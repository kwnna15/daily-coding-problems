from asteroid import collision


def test_example_1():
    asteroids = [5, 10, -5]
    assert collision(asteroids) == [5, 10]


def test_example_2():
    asteroids = [8, -8]
    assert collision(asteroids) == []


def test_example_3():
    asteroids = [10, 2, -5]
    assert collision(asteroids) == [10]


def test_example_4():
    asteroids = [-2, -1, 1, 2]
    assert collision(asteroids) == [-2, -1, 1, 2]


def test_example_5():
    asteroids = [1, -1, 2, -2]
    assert collision(asteroids) == []
