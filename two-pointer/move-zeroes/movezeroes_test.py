import pytest
from movezeroes import move_zeroes


def test_example_1():
    nums = [0, 1, 0, 3, 12]
    move_zeroes(nums)
    assert nums == [1, 3, 12, 0, 0]


def test_example_2():
    nums = [0, 0, 1]
    move_zeroes(nums)
    assert nums == [1, 0, 0]


def test_example_3():
    nums = [4, 2, 4, 0, 0, 3, 0, 5, 1, 0]
    move_zeroes(nums)
    assert nums == [4, 2, 4, 3, 5, 1, 0, 0, 0, 0]


def test_example_4():
    nums = [0, 0, 0, 0, 0]
    move_zeroes(nums)
    assert nums == [0, 0, 0, 0, 0]


def test_example_5():
    nums = [1, 2, 3, 4, 5]
    move_zeroes(nums)
    assert nums == [1, 2, 3, 4, 5]


if __name__ == "__main__":
    pytest.main()
