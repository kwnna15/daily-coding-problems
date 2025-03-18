from numprovinces import Solution


def test_example_1():
    isConnected = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
    sol = Solution()
    assert sol.count(isConnected) == 2


def test_example_2():
    isConnected = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    sol = Solution()
    assert sol.count(isConnected) == 3


def test_example_3():
    isConnected = [[1, 1, 0, 0], [1, 1, 0, 0], [0, 0, 1, 1], [0, 0, 1, 1]]
    sol = Solution()
    assert sol.count(isConnected) == 2


def test_example_4():
    isConnected = [[1]]
    sol = Solution()
    assert sol.count(isConnected) == 1


def test_example_5():
    isConnected = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
    sol = Solution()
    assert sol.count(isConnected) == 1
