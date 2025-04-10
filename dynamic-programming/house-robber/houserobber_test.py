from houserobber import Solution


def test_example_1():
    nums = [1, 2, 3, 1]
    sol = Solution()
    assert sol.rob(nums) == 4


def test_example_2():
    nums = [2, 7, 9, 3, 1]
    sol = Solution()
    assert sol.rob(nums) == 12


def test_example_3():
    nums = [0]
    sol = Solution()
    assert sol.rob(nums) == 0


def test_example_4():
    nums = [2, 1, 1, 2]
    sol = Solution()
    assert sol.rob(nums) == 4


def test_example_5():
    nums = [5, 5, 10, 100, 10, 5]
    sol = Solution()
    assert sol.rob(nums) == 110
