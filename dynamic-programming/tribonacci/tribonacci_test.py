from tribonacci import Solution


def test_example_1():
    n = 0
    sol = Solution()
    assert sol.tribonacci(n) == 0


def test_example_2():
    n = 1
    sol = Solution()
    assert sol.tribonacci(n) == 1


def test_example_3():
    n = 2
    sol = Solution()
    assert sol.tribonacci(n) == 1


def test_example_4():
    n = 10
    sol = Solution()
    assert sol.tribonacci(n) == 149


def test_example_5():
    n = 25
    sol = Solution()
    assert sol.tribonacci(n) == 1389537
