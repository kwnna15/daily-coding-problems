from climbingstairs import Solution


def test_example_1():
    cost = [10, 15, 20]
    sol = Solution()
    assert sol.mincost(cost) == 15


def test_example_2():
    cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    sol = Solution()
    assert sol.mincost(cost) == 6


def test_example_3():
    cost = [0, 0, 0, 0]
    sol = Solution()
    assert sol.mincost(cost) == 0


def test_example_4():
    cost = [10, 15]
    sol = Solution()
    assert sol.mincost(cost) == 10


def test_example_5():
    cost = [1]
    sol = Solution()
    assert sol.mincost(cost) == 0
