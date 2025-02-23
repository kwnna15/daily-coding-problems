def index(nums: list[int]) -> int:
    left, right = 0, sum(nums)
    for idx, ele in enumerate(nums):
        right -= ele
        if left == right:
            return idx
        left += ele
    return -1
