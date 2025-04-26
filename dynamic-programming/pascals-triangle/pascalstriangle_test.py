from pascalstriangle import Solution


def test_example_1():
    numRows = 5
    sol = Solution()
    assert sol.generate(numRows) == [
        [1],
        [1, 1],
        [1, 2, 1],
        [1, 3, 3, 1],
        [1, 4, 6, 4, 1],
    ]


def test_example_2():
    numRows = 1
    sol = Solution()
    assert sol.generate(numRows) == [[1]]


def test_example_3():
    numRows = 3
    sol = Solution()
    assert sol.generate(numRows) == [[1], [1, 1], [1, 2, 1]]


def test_example_4():
    numRows = 2
    sol = Solution()
    assert sol.generate(numRows) == [[1], [1, 1]]


def test_example_5():
    numRows = 6
    sol = Solution()
    assert sol.generate(numRows) == [
        [1],
        [1, 1],
        [1, 2, 1],
        [1, 3, 3, 1],
        [1, 4, 6, 4, 1],
        [1, 5, 10, 10, 5, 1],
    ]
