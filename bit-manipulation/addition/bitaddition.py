class Solution:
    def add(self, a: str, b: str) -> str:
        return bin(int(a,2) + int(b,2))[2:]