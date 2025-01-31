import sys


def findDifference(nums1: list[int], nums2: list[int]) -> list[list[int]]:
    set1 = set(nums1)
    set2 = set(nums2)
    ans1 = []
    ans2 = []

    for i in set2:
        if i not in set1:
            ans2.append(i)

    for j in set1:
        if j not in set2:
            ans1.append(j)

    return [ans1, ans2]


if __name__ == "__main__":
    nums1 = list(map(int, sys.argv[1].split(",")))
    nums2 = list(map(int, sys.argv[2].split(",")))
    print(findDifference(nums1, nums2))
