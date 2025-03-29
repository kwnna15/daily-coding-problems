from successfulpairs import Solution


def test_example_1():
    spells = [10, 20, 30]
    potions = [1, 2, 3, 4, 5]
    success = 20
    sol = Solution()
    assert sol.calculate(spells, potions, success) == [4, 5, 5]


def test_example_2():
    spells = [5, 1, 3]
    potions = [1, 2, 3, 4, 5]
    success = 7
    sol = Solution()
    assert sol.calculate(spells, potions, success) == [4, 0, 3]


def test_example_3():
    spells = [10, 20]
    potions = [5, 5, 5]
    success = 50
    sol = Solution()
    assert sol.calculate(spells, potions, success) == [3, 3]


def test_example_4():
    spells = [1, 2, 3]
    potions = [8, 5, 8]
    success = 16
    sol = Solution()
    assert sol.calculate(spells, potions, success) == [0, 2, 2]


def test_example_5():
    spells = [10]
    potions = [1, 2, 3, 4, 5]
    success = 100
    sol = Solution()
    assert sol.calculate(spells, potions, success) == [0]
