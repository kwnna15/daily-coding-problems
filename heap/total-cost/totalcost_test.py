from totalcost import Solution


def test_example_1():
    costs = [17, 12, 10, 2, 7, 2, 11, 20, 8]
    k = 3
    candidates = 4
    sol = Solution()
    assert sol.calculate(costs, k, candidates) == 11


def test_example_2():
    costs = [1, 2, 4, 1]
    k = 3
    candidates = 3
    sol = Solution()
    assert sol.calculate(costs, k, candidates) == 4


def test_example_3():
    costs = [5, 5, 5, 5, 5]
    k = 2
    candidates = 2
    sol = Solution()
    assert sol.calculate(costs, k, candidates) == 10


def test_example_4():
    costs = [10, 20, 30, 40, 50]
    k = 1
    candidates = 3
    sol = Solution()
    assert sol.calculate(costs, k, candidates) == 10


def test_example_5():
    costs = [7, 3, 5, 1, 6, 4, 2]
    k = 4
    candidates = 2
    sol = Solution()
    assert sol.calculate(costs, k, candidates) == 10
