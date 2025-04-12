from bitcounter import Solution


def test_example_1():
    n = 2
    sol = Solution()
    assert sol.count(n) == [0, 1, 1]


def test_example_2():
    n = 5
    sol = Solution()
    assert sol.count(n) == [0, 1, 1, 2, 1, 2]


def test_example_3():
    n = 0
    sol = Solution()
    assert sol.count(n) == [0]


def test_example_4():
    n = 10
    sol = Solution()
    assert sol.count(n) == [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2]


def test_example_5():
    n = 1
    sol = Solution()
    assert sol.count(n) == [0, 1]
