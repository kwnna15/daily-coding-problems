from stringcompression import compress

def test_example_1():
    chars = ["a","a","b","b","c","c","c"]
    assert compress(chars) == 6
    assert chars[:6] == ["a","2","b","2","c","3"]

def test_example_2():
    chars = ["a"]
    assert compress(chars) == 1
    assert chars[:1] == ["a"]

def test_example_3():
    chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
    assert compress(chars) == 4
    assert chars[:4] == ["a","b","1","2"]

def test_example_4():
    chars = ["a","a","a","b","b","a","a"]
    assert compress(chars) == 6
    assert chars[:6] == ["a","3","b","2","a","2"]

def test_example_5():
    chars = ["a","a","a","a","a","a","a","a","a","a"]
    assert compress(chars) == 3
    assert chars[:3] == ["a","1","0"]