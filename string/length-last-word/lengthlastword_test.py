from lengthlastword import Solution


def test_example_1():
    s = "Hello World"
    sol = Solution()
    assert sol.length(s) == 5


def test_example_2():
    s = "   fly me   to   the moon  "
    sol = Solution()
    assert sol.length(s) == 4


def test_example_3():
    s = "luffy is still joyboy"
    sol = Solution()
    assert sol.length(s) == 6


def test_example_4():
    s = "a"
    sol = Solution()
    assert sol.length(s) == 1


def test_example_5():
    s = "   one   "
    sol = Solution()
    assert sol.length(s) == 3
