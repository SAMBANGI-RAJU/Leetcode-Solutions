class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        q = deque()
        d = [[-1]*m for _ in range(n)]
        def isValid(i, j):
            return 0<=i<n and 0<=j<m
        

        direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    q.append([i, j])
                    d[i][j] = 0
        

        if (len(q) == 0) | (len(q) == m*n):
            return -1
        
        ans = 0
        while q:
            i, j = q.pop()
            for dx, dy in direction:
                x = i+dx
                y = j+dy 
                if isValid(x, y) and d[x][y]<0:
                    q.appendleft([x, y])
                    d[x][y] = d[i][j] + 1
                    ans = max(ans, d[x][y])
        return ans