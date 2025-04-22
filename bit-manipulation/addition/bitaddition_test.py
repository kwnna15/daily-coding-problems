from bitaddition import Solution


def test_example_1():
    a = "11"
    b = "1"
    sol = Solution()
    assert sol.add(a, b) == "100"


def test_example_2():
    a = "1010"
    b = "1011"
    sol = Solution()
    assert sol.add(a, b) == "10101"


def test_example_3():
    a = "0"
    b = "0"
    sol = Solution()
    assert sol.add(a, b) == "0"


def test_example_4():
    a = "111"
    b = "1"
    sol = Solution()
    assert sol.add(a, b) == "1000"


def test_example_5():
    a = "1"
    b = "111"
    sol = Solution()
    assert sol.add(a, b) == "1000"
