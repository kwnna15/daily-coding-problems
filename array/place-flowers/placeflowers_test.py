from placeflowers import place_flowers

def test_example_1():
    flowerbed = [1, 0, 0, 0, 1]
    n = 1
    assert place_flowers(flowerbed, n) == True

def test_example_2():
    flowerbed = [1, 0, 0, 0, 1]
    n = 2
    assert place_flowers(flowerbed, n) == False

def test_example_3():
    flowerbed = [0, 0, 1, 0, 0]
    n = 1
    assert place_flowers(flowerbed, n) == True

def test_example_4():
    flowerbed = [0, 0, 1, 0, 1]
    n = 2
    assert place_flowers(flowerbed, n) == False

def test_example_5():
    flowerbed = [1, 0, 0, 0, 0, 1]
    n = 2
    assert place_flowers(flowerbed, n) == False