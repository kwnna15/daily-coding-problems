def max_operations(nums: list[int], k: int) -> int:
    i = 0
    j = len(nums) - 1
    count = 0
    nums.sort()
    while j > i:
        if nums[i] + nums[j] > k:
            j = j - 1
        elif nums[i] + nums[j] < k:
            i = i + 1
        else:
            count = count + 1
            nums[i] = nums[j] = 0
            i = i + 1
            j = j - 1
    return count
