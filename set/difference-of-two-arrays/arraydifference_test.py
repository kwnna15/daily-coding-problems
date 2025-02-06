from arraydifference import array_difference


def test_example_1():
    nums1 = [1, 2, 3]
    nums2 = [2, 4, 6]
    assert array_difference(nums1, nums2) == [[1, 3], [4, 6]]


def test_example_2():
    nums1 = [1, 2, 3, 4]
    nums2 = [3, 4, 5, 6]
    assert array_difference(nums1, nums2) == [[1, 2], [5, 6]]


def test_example_3():
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    assert array_difference(nums1, nums2) == [[1], []]


def test_example_4():
    nums1 = [4, 9, 5]
    nums2 = [9, 4, 9, 8, 4]
    assert array_difference(nums1, nums2) == [[5], [8]]


def test_example_5():
    nums1 = [1, 2, 3, 4, 5]
    nums2 = [6, 7, 8, 9, 10]
    assert array_difference(nums1, nums2) == [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
