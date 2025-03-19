from reorderroutes import Solution


def test_example_1():
    n = 6
    connections = [[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]]
    sol = Solution()
    assert sol.reorder(n, connections) == 3


def test_example_2():
    n = 5
    connections = [[1, 0], [1, 2], [3, 2], [3, 4]]
    sol = Solution()
    assert sol.reorder(n, connections) == 2


def test_example_3():
    n = 3
    connections = [[1, 0], [2, 0]]
    sol = Solution()
    assert sol.reorder(n, connections) == 0


def test_example_4():
    n = 4
    connections = [[0, 1], [2, 0], [3, 2]]
    sol = Solution()
    assert sol.reorder(n, connections) == 1


def test_example_5():
    n = 3
    connections = [[0, 1], [1, 2], [2, 3], [4, 5], [5, 6], [6, 4]]
    sol = Solution()
    assert sol.reorder(n, connections) == 3
