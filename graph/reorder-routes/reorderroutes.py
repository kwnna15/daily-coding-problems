class Solution:
    def reorder(self, n: int, connections: list[list[int]]) -> int:
        seen, ans = {0}, 0
        
        while len(seen) < n:
            check = []
            for path in connections:
                if path[1] in seen:
                    seen.add(path[0])
                elif path[0] in seen:
                    seen.add(path[1])
                    ans += 1
                else:
                    check.append(path)
            connections = check[::-1]
        
        return ans