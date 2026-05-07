class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        r = len(grid)
        c = len(grid[0])
        direc = [(0, 1), (1,0), (-1,0), (0, -1)]
        curr_area = 0
        count = 0     

        def dfs(grid, rows, cols):
            nonlocal curr_area
            if grid[rows][cols] == 1:
                curr_area += 1
                grid[rows][cols] = 0
                for dr, dc in direc:
                    nr, nc = dr + rows, dc + cols
                    if 0 <= nr < r and 0 <= nc < c:
                        dfs(grid, nr, nc)

        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    dfs(grid, i, j)
                    count = max(count, curr_area)
                    curr_area = 0
        return count