from dominotiling import Solution


def test_example_1():
    n = 3
    sol = Solution()
    assert sol.tilings(n) == 5


def test_example_2():
    n = 1
    sol = Solution()
    assert sol.tilings(n) == 1


def test_example_3():
    n = 4
    sol = Solution()
    assert sol.tilings(n) == 11


def test_example_4():
    n = 0
    sol = Solution()
    assert sol.tilings(n) == 1


def test_example_5():
    n = 5
    sol = Solution()
    assert sol.tilings(n) == 24
