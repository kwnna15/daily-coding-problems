from keysandrooms import Solution


def test_example_1():
    rooms = [[1], [2], [3], []]
    sol = Solution()
    assert sol.visit(rooms) == True


def test_example_2():
    rooms = [[1, 3], [3, 0, 1], [2], [0]]
    sol = Solution()
    assert sol.visit(rooms) == False


def test_example_3():
    rooms = [[1, 2, 3], [0], [0], [0]]
    sol = Solution()
    assert sol.visit(rooms) == True


def test_example_4():
    rooms = [[1], [2], [3], [4], []]
    sol = Solution()
    assert sol.visit(rooms) == True


def test_example_5():
    rooms = [[2, 3], [], [4], [5], [6], [7], [6], [1], []]
    sol = Solution()
    assert sol.visit(rooms) == False
