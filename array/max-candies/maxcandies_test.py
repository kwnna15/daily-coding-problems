from maxcandies import max_candies

def test_example_1():
    candies = [1, 2, 3, 4, 5]
    k = 3
    assert max_candies(candies, k) == [False, True, True, True, True]

def test_example_2():
    candies = [5, 5, 5, 5]
    k = 2
    assert max_candies(candies, k) == [True, True, True, True]

def test_example_3():
    candies = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    k = 5
    assert max_candies(candies, k) == [False, False, False, False, True, True, True, True, True, True]

def test_example_4():
    candies = [10, 20, 30, 40, 50]
    k = 4
    assert max_candies(candies, k) == [False, False, False, False, True]

def test_example_5():
    candies = [1, 1, 1, 1, 1]
    k = 1
    assert max_candies(candies, k) == [True, True, True, True, True]