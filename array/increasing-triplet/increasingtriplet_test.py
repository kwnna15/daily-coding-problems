from increasingtriplet import increasing_triplet


def test_example_1():
    nums = [1, 2, 3, 4, 5]
    assert increasing_triplet(nums) == True


def test_example_2():
    nums = [5, 4, 3, 2, 1]
    assert increasing_triplet(nums) == False


def test_example_3():
    nums = [2, 1, 5, 0, 4, 6]
    assert increasing_triplet(nums) == True


def test_example_4():
    nums = [20, 100, 10, 12, 5, 13]
    assert increasing_triplet(nums) == True


def test_example_5():
    nums = [2, 2, 3, 3, 2, 2, 2, 3, 1]
    assert increasing_triplet(nums) == False
