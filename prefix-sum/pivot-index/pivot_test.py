from pivot import index

def test_example_1():
    nums = [1, 7, 3, 6, 5, 6]
    assert index(nums) == 3

def test_example_2():
    nums = [1, 2, 3]
    assert index(nums) == -1

def test_example_3():
    nums = [2, 1, -1]
    assert index(nums) == 0

def test_example_4():
    nums = [0, 0, 0, 0, 1]
    assert index(nums) == 4

def test_example_6():
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert index(nums) == -1