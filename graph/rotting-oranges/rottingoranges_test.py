from rottingoranges import Solution


def test_example_1():
    grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
    sol = Solution()
    assert sol.calculate(grid) == 4


def test_example_2():
    grid = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]
    sol = Solution()
    assert sol.calculate(grid) == -1


def test_example_3():
    grid = [[0, 2]]
    sol = Solution()
    assert sol.calculate(grid) == 0


def test_example_4():
    grid = [[2, 1, 1, 0, 2], [1, 1, 0, 1, 1], [0, 1, 2, 1, 1], [1, 0, 1, 1, 2]]
    sol = Solution()
    assert sol.calculate(grid) == -1


def test_example_5():
    grid = [[0, 0, 0], [0, 2, 0], [0, 0, 0]]
    sol = Solution()
    assert sol.calculate(grid) == 0
