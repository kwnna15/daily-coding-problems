def equal_pairs(grid: list[list[int]]) -> int:
    nrows = len(grid)  
    count = 0
    for r in range(nrows):
        for c in range(nrows):
            if all(grid[r][k] == grid[k][c] for k in range(nrows)):
                count += 1
    return count
