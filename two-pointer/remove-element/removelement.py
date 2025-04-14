class Solution:
    def remove(self, nums: list[int], val: int) -> int:
        temp = []
        for num in nums:
            if num != val:
                temp.append(num)
        nums[:] = temp
        return len(nums)
