from removelement import Solution


def test_example_1():
    nums = [3, 2, 2, 3]
    val = 3
    sol = Solution()
    length = sol.remove(nums, val)
    assert length == 2
    assert sorted(nums[:length]) == [2, 2]


def test_example_2():
    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    val = 2
    sol = Solution()
    length = sol.remove(nums, val)
    assert length == 5
    assert sorted(nums[:length]) == [0, 0, 1, 3, 4]


def test_example_3():
    nums = [1]
    val = 1
    sol = Solution()
    length = sol.remove(nums, val)
    assert length == 0
    assert nums[:length] == []


def test_example_4():
    nums = [4, 5]
    val = 5
    sol = Solution()
    length = sol.remove(nums, val)
    assert length == 1
    assert nums[:length] == [4]


def test_example_5():
    nums = [2, 2, 2, 2]
    val = 2
    sol = Solution()
    length = sol.remove(nums, val)
    assert length == 0
    assert nums[:length] == []
