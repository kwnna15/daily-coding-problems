class Solution:
    def guessnum(self, n: int) -> int:
        left, right = 1, n
        while left < right:
            mid = (left + right) // 2
            if self.guess(mid) == 0:
                return mid
            elif self.guess(mid) == -1:
                right = mid - 1
            else:
                left = mid + 1
        return left

    def guess(num: int) -> int:
        if num == 7:
            return 0
        elif num < 7:
            return 1
        else:
            return -1
