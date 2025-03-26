from subsequencescore import Solution


def test_example_1():
    nums1 = [1, 3, 3, 2]
    nums2 = [2, 1, 3, 4]
    k = 3
    sol = Solution()
    assert sol.max(nums1, nums2, k) == 12


def test_example_2():
    nums1 = [4, 2, 3, 1]
    nums2 = [2, 3, 1, 4]
    k = 2
    sol = Solution()
    assert sol.max(nums1, nums2, k) == 12


def test_example_3():
    nums1 = [5, 1, 3]
    nums2 = [3, 4, 2]
    k = 2
    sol = Solution()
    assert sol.max(nums1, nums2, k) == 18


def test_example_4():
    nums1 = [1, 2, 3, 4]
    nums2 = [4, 3, 2, 1]
    k = 1
    sol = Solution()
    assert sol.max(nums1, nums2, k) == 6


def test_example_5():
    nums1 = [10, 20, 30]
    nums2 = [1, 2, 3]
    k = 2
    sol = Solution()
    assert sol.max(nums1, nums2, k) == 100
