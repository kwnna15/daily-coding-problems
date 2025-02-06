from uniqueoccurrences import unique_occurrences


def test_example_1():
    arr = [1, 2, 2, 1, 1, 3]
    assert unique_occurrences(arr) == True


def test_example_2():
    arr = [1, 2]
    assert unique_occurrences(arr) == False


def test_example_3():
    arr = [-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]
    assert unique_occurrences(arr) == True


def test_example_4():
    arr = [1, 2, 2, 3, 3, 3]
    assert unique_occurrences(arr) == True


def test_example_5():
    arr = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
    assert unique_occurrences(arr) == True
