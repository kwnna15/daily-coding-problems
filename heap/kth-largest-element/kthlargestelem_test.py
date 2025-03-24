from kthlargestelem import Solution


def test_example_1():
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    sol = Solution()
    assert sol.find(nums, k) == 5


def test_example_2():
    nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k = 4
    sol = Solution()
    assert sol.find(nums, k) == 4


def test_example_3():
    nums = [1]
    k = 1
    sol = Solution()
    assert sol.find(nums, k) == 1


def test_example_4():
    nums = [7, 10, 4, 3, 20, 15]
    k = 3
    sol = Solution()
    assert sol.find(nums, k) == 10


def test_example_5():
    nums = [5, 5, 5, 5, 5]
    k = 2
    sol = Solution()
    assert sol.find(nums, k) == 5
