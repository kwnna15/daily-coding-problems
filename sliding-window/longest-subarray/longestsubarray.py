def longest(nums: list[int]) -> int:
    zeros, left, right = 0, 0, 0
    while right < len(nums):
        if nums[right] == 0:
            zeros += 1
        if zeros > 1:
            left += 1
            if nums[left - 1] == 0:
                zeros -= 1
        right += 1
    return (right - left) - 1
