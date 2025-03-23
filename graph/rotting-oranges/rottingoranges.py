class Solution:
    def calculate(self, grid: list[list[int]]) -> int:
        visited, curr = set(), []

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    visited.add((i, j))
                elif grid[i][j] == 2:
                    curr.append((i, j))

        result = 0
        while visited and curr:
            newr = []
            for i, j in curr:
                for coord in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                    if coord in visited:
                        visited.remove(coord)
                        newr.append(coord)
            curr = newr
            result += 1

        return -1 if visited else result
