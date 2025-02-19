from consecutiveones import longest


def test_example_1():
    nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
    k = 2
    assert longest(nums, k) == 6


def test_example_2():
    nums = [0, 0, 1, 1, 1, 0, 0]
    k = 0
    assert longest(nums, k) == 3


def test_example_3():
    nums = [1, 1, 1, 1, 1]
    k = 0
    assert longest(nums, k) == 5


def test_example_4():
    nums = [0, 0, 0, 0, 0]
    k = 5
    assert longest(nums, k) == 5


def test_example_5():
    nums = [1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1]
    k = 3
    assert longest(nums, k) == 11
