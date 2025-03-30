from peakelement import Solution


def test_example_1():
    nums = [1, 2, 3, 1]
    sol = Solution()
    result = sol.find(nums)
    assert result in [2]  # Peak element is at index 2


def test_example_2():
    nums = [1, 2, 1, 3, 5, 6, 4]
    sol = Solution()
    result = sol.find(nums)
    assert result in [1, 5]  # Peak elements are at index 1 or 5


def test_example_3():
    nums = [1]
    sol = Solution()
    result = sol.find(nums)
    assert result == 0  # Single element is the peak


def test_example_4():
    nums = [1, 2]
    sol = Solution()
    result = sol.find(nums)
    assert result == 1  # Peak element is at index 1


def test_example_5():
    nums = [2, 1]
    sol = Solution()
    result = sol.find(nums)
    assert result == 0  # Peak element is at index 0
