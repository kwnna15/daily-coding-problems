from kokoeating import Solution


def test_example_1():
    piles = [3, 6, 7, 11]
    h = 8
    sol = Solution()
    assert sol.speed(piles, h) == 4


def test_example_2():
    piles = [30, 11, 23, 4, 20]
    h = 5
    sol = Solution()
    assert sol.speed(piles, h) == 30


def test_example_3():
    piles = [30, 11, 23, 4, 20]
    h = 6
    sol = Solution()
    assert sol.speed(piles, h) == 23


def test_example_4():
    piles = [1, 1, 1, 1]
    h = 4
    sol = Solution()
    assert sol.speed(piles, h) == 1


def test_example_5():
    piles = [1000000000]
    h = 1
    sol = Solution()
    assert sol.speed(piles, h) == 1000000000
