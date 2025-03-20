from nearestexit import Solution


def test_example_1():
    maze = [["+", "+", ".", "+"], [".", ".", ".", "+"], ["+", "+", "+", "."]]
    entrance = [1, 2]
    sol = Solution()
    assert sol.calculate(maze, entrance) == 1


def test_example_2():
    maze = [["+", "+", "+"], [".", ".", "."], ["+", "+", "+"]]
    entrance = [1, 0]
    sol = Solution()
    assert sol.calculate(maze, entrance) == 2


def test_example_3():
    maze = [[".", "+"]]
    entrance = [0, 0]
    sol = Solution()
    assert sol.calculate(maze, entrance) == -1


def test_example_4():
    maze = [
        ["+", ".", "+", "+", "+", "+", "+"],
        ["+", ".", "+", ".", ".", ".", "+"],
        ["+", ".", "+", ".", "+", ".", "+"],
        ["+", ".", ".", ".", "+", ".", "+"],
        ["+", "+", "+", "+", "+", ".", "+"],
    ]
    entrance = [0, 1]
    sol = Solution()
    assert sol.calculate(maze, entrance) == 12


def test_example_5():
    maze = [
        ["+", "+", "+", "+", "+", "+", "+"],
        ["+", ".", ".", ".", ".", ".", "+"],
        ["+", ".", "+", "+", "+", ".", "+"],
        ["+", ".", ".", ".", "+", ".", "+"],
        ["+", "+", "+", "+", "+", ".", "+"],
    ]
    entrance = [1, 1]
    sol = Solution()
    assert sol.calculate(maze, entrance) == 7
