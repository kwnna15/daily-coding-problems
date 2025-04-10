class Solution:
    def rob(self, nums: list[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        if n == 1:
            return nums[0]
        prev1, prev2 = nums[0], 0
        for i in range(1, n):
            current = max(prev1, nums[i] + prev2)
            prev2 = prev1
            prev1 = current
        return prev1
