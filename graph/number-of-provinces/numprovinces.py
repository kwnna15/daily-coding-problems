class Solution:
    def count(self, isConnected: list[list[int]]) -> int:
        if not isConnected:
            return 0

        n = len(isConnected)
        visited = [0] * n

        def dfs(node):
            for i in range(n):
                if isConnected[node][i] == 1 and not visited[i]:
                    visited[i] = 1
                    dfs(i)

        count = 0
        for i in range(n):
            if not visited[i]:
                visited[i] = 1
                count += 1
                dfs(i)

        return count
