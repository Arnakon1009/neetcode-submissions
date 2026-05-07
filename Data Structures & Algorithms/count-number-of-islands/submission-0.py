class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        direct = [(0,1), (1,0), (0,-1), (-1,0)]
        def dfs(grid,r1, c1):
            if grid[r1][c1] == "1":
                grid[r1][c1] = "0"
                for dr, dc in direct:
                    nr, nc = dr + r1, dc + c1
                    if 0 <= nr < r and 0 <= nc < c:
                        dfs(grid, nr, nc)

        r = len(grid)
        c = len(grid[0])
        for i in range(r):
            for j in range(c):
                if grid[i][j] == "1":
                    count += 1
                    dfs(grid, i, j)
        return count