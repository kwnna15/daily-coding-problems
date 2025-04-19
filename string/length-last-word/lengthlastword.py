class Solution:
    def length(self, s: str) -> int:
        return len(s.strip().split()[-1])
