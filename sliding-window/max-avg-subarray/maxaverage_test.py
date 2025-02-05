import pytest
from maxaverage import max_average


def test_example_1():
    nums = [1, 12, -5, -6, 50, 3]
    k = 4
    assert max_average(nums, k) == 12.75


def test_example_2():
    nums = [5, 5, 5, 5]
    k = 2
    assert max_average(nums, k) == 5.0


def test_example_3():
    nums = [0, 4, 0, 3, 2]
    k = 1
    assert max_average(nums, k) == 4.0


def test_example_4():
    nums = [1, 2, 3, 4, 5]
    k = 3
    assert max_average(nums, k) == 4.0


def test_example_5():
    nums = [7, 8, 8, 7, 6, 5, 4, 3, 2, 1]
    k = 5
    assert max_average(nums, k) == 7.2
