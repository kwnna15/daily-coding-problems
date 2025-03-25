from infiniteset import SmallestInfiniteSet


def test_example_1():
    obj = SmallestInfiniteSet()
    assert obj.pop() == 1
    assert obj.pop() == 2
    obj.add(1)
    assert obj.pop() == 1
    assert obj.pop() == 3


def test_example_2():
    obj = SmallestInfiniteSet()
    obj.add(2)
    assert obj.pop() == 1
    assert obj.pop() == 2
    assert obj.pop() == 3


def test_example_3():
    obj = SmallestInfiniteSet()
    obj.add(5)
    obj.add(3)
    assert obj.pop() == 1
    assert obj.pop() == 2
    assert obj.pop() == 3
    assert obj.pop() == 4
    assert obj.pop() == 5


def test_example_4():
    obj = SmallestInfiniteSet()
    obj.add(2)
    obj.add(2)  # Adding duplicate, should not affect the set
    assert obj.pop() == 1
    assert obj.pop() == 2
    assert obj.pop() == 3


def test_example_5():
    obj = SmallestInfiniteSet()
    obj.add(10)
    obj.add(5)
    obj.add(7)
    assert obj.pop() == 1
    assert obj.pop() == 2
    assert obj.pop() == 3
    assert obj.pop() == 4
    assert obj.pop() == 5
    assert obj.pop() == 6
    assert obj.pop() == 7
    assert obj.pop() == 8
