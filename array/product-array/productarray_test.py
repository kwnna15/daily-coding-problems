from productarray import product_array


def test_example_1():
    nums = [1, 2, 3, 4]
    assert product_array(nums) == [24, 12, 8, 6]


def test_example_2():
    nums = [5, 6, 2, 3]
    assert product_array(nums) == [36, 30, 90, 60]


def test_example_3():
    nums = [1, 2, 3, 4, 5]
    assert product_array(nums) == [120, 60, 40, 30, 24]


def test_example_4():
    nums = [10, 3, 5, 6, 2]
    assert product_array(nums) == [180, 600, 360, 300, 900]


def test_example_5():
    nums = [1, 1, 1, 1]
    assert product_array(nums) == [1, 1, 1, 1]
