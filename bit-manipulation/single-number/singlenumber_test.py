from singlenumber import Solution


def test_example_1():
    nums = [2, 2, 1]
    sol = Solution()
    assert sol.number(nums) == 1


def test_example_2():
    nums = [4, 1, 2, 1, 2]
    sol = Solution()
    assert sol.number(nums) == 4


def test_example_3():
    nums = [1]
    sol = Solution()
    assert sol.number(nums) == 1


def test_example_4():
    nums = [0, 0, 0, 7]
    sol = Solution()
    assert sol.number(nums) == 7


def test_example_5():
    nums = [10, 10, 20, 20, 30]
    sol = Solution()
    assert sol.number(nums) == 30
