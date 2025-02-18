from ksumpairs import max_operations

def test_example_1():
    nums = [1, 2, 3, 4]
    k = 5
    assert max_operations(nums, k) == 2

def test_example_2():
    nums = [3, 1, 3, 4, 3]
    k = 6
    assert max_operations(nums, k) == 1

def test_example_3():
    nums = [1, 2, 3, 4, 5, 6]
    k = 7
    assert max_operations(nums, k) == 3

def test_example_4():
    nums = [1, 1, 1, 1]
    k = 2
    assert max_operations(nums, k) == 2

def test_example_5():
    nums = [2, 2, 2, 2]
    k = 4
    assert max_operations(nums, k) == 2