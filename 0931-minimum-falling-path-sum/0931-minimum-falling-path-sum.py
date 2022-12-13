class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m,n=len(matrix),len(matrix[0])
        for i in range(m-2,-1,-1):
            for j in range(n):
                a,b=float('inf'),float('inf')
                if j>0:
                    a=matrix[i+1][j-1]
                if j<n-1:
                    b=matrix[i+1][j+1]
                matrix[i][j]+=min(a,matrix[i+1][j],b)
        return min([i for i in matrix[0]])