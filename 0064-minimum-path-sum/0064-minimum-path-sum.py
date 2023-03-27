class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        cur = [grid[0][0]] * m
        
        for i in range(1, m):
            cur[i] = cur[i - 1] + grid[i][0]
        
        for j in range(1, n):
            cur[0] += grid[0][j]
            for i in range(1, m):
                cur[i] = min(cur[i - 1], cur[i]) + grid[i][j]
        
        return cur[m - 1]