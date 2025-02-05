import pytest
from sumtok import sum_to_k


def test_example_1():
    nums = [10, 15, 3, 7]
    k = 17
    result = sum_to_k(nums, k)
    assert result is not None
    assert set(result) == {10, 7}


def test_example_2():
    nums = [1, 2, 3, 4]
    k = 8
    assert sum_to_k(nums, k) == None


def test_example_3():
    nums = [1, 2, 3, 4, 5]
    k = 9
    result = sum_to_k(nums, k)
    assert result is not None
    assert set(result) == {4, 5}


def test_example_4():
    nums = [1, 2, 3, 4, 5]
    k = 10
    assert sum_to_k(nums, k) == None


def test_example_5():
    nums = [5, 5, 5, 5]
    k = 10
    result = sum_to_k(nums, k)
    assert result is not None
    assert set(result) == {5, 5}
