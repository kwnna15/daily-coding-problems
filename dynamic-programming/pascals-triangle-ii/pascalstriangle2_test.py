from pascalstriangle2 import Solution


def test_example_1():
    rowIndex = 3
    sol = Solution()
    assert sol.row(rowIndex) == [1, 3, 3, 1]


def test_example_2():
    rowIndex = 0
    sol = Solution()
    assert sol.row(rowIndex) == [1]


def test_example_3():
    rowIndex = 1
    sol = Solution()
    assert sol.row(rowIndex) == [1, 1]


def test_example_4():
    rowIndex = 4
    sol = Solution()
    assert sol.row(rowIndex) == [1, 4, 6, 4, 1]


def test_example_5():
    rowIndex = 5
    sol = Solution()
    assert sol.row(rowIndex) == [1, 5, 10, 10, 5, 1]
