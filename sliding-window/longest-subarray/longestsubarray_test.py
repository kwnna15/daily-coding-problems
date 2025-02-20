from longestsubarray import longest


def test_example_1():
    nums = [1, 1, 0, 1]
    assert longest(nums) == 3


def test_example_2():
    nums = [0, 1, 1, 1, 0, 1, 1, 0, 1]
    assert longest(nums) == 5


def test_example_3():
    nums = [1, 1, 1, 1, 1]
    assert longest(nums) == 4


def test_example_4():
    nums = [0, 0, 0, 0, 0]
    assert longest(nums) == 0


def test_example_6():
    nums = [1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1]
    assert longest(nums) == 5
