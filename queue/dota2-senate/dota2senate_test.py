from dota2senate import predict


def test_example_1():
    senate = "RD"
    assert predict(senate) == "Radiant"


def test_example_2():
    senate = "RDD"
    assert predict(senate) == "Dire"


def test_example_3():
    senate = "RRDDD"
    assert predict(senate) == "Radiant"


def test_example_4():
    senate = "RDRDR"
    assert predict(senate) == "Radiant"


def test_example_5():
    senate = "DDRRRRRDDRDRDDDR"
    assert predict(senate) == "Radiant"
