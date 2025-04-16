from searchinsert import Solution


def test_example_1():
    nums = [1, 3, 5, 6]
    target = 5
    sol = Solution()
    assert sol.search(nums, target) == 2


def test_example_2():
    nums = [1, 3, 5, 6]
    target = 2
    sol = Solution()
    assert sol.search(nums, target) == 1


def test_example_3():
    nums = [1, 3, 5, 6]
    target = 7
    sol = Solution()
    assert sol.search(nums, target) == 4


def test_example_4():
    nums = [1, 3, 5, 6]
    target = 0
    sol = Solution()
    assert sol.search(nums, target) == 0


def test_example_5():
    nums = [1]
    target = 0
    sol = Solution()
    assert sol.search(nums, target) == 0
