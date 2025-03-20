from collections import deque


class Solution:
    def calculate(self, maze: list[list[str]], entrance: list[int]) -> int:
        rows = len(maze)
        columns = len(maze[0])

        queue = deque([(entrance[0], entrance[1], 0)])
        maze[entrance[0]][entrance[1]] = "+"

        while queue:
            row, col, steps = queue.popleft()

            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nr, nc = row + dy, col + dx
                if 0 <= nr < rows and 0 <= nc < columns and maze[nr][nc] == ".":
                    if (nr == 0 or nr == rows - 1) or (nc == 0 or nc == columns - 1):
                        return steps + 1

                    maze[nr][nc] = "+"
                    queue.append((nr, nc, steps + 1))

        return -1
