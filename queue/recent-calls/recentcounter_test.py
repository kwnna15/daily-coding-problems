from recentcounter import RecentCounter


def test_example_1():
    rc = RecentCounter()
    assert rc.ping(1) == 1
    assert rc.ping(100) == 2
    assert rc.ping(3001) == 3
    assert rc.ping(3002) == 3


def test_example_2():
    rc = RecentCounter()
    assert rc.ping(1) == 1
    assert rc.ping(2) == 2
    assert rc.ping(3001) == 3
    assert rc.ping(6000) == 2


def test_example_3():
    rc = RecentCounter()
    assert rc.ping(100) == 1
    assert rc.ping(200) == 2
    assert rc.ping(300) == 3
    assert rc.ping(400) == 4
    assert rc.ping(5000) == 1


def test_example_4():
    rc = RecentCounter()
    assert rc.ping(1) == 1
    assert rc.ping(3000) == 2
    assert rc.ping(6000) == 2
    assert rc.ping(9000) == 2


def test_example_5():
    rc = RecentCounter()
    assert rc.ping(1) == 1
    assert rc.ping(100) == 2
    assert rc.ping(200) == 3
    assert rc.ping(3000) == 4
    assert rc.ping(3001) == 5
    assert rc.ping(6000) == 3
