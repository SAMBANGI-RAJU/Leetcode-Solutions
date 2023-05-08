class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sum=0
        c=len(mat[0])
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if i==j:
                    sum+=mat[i][j]
                 
        x=0
        y=len(mat)-1
        res=0
        while y>=0:
            res+=mat[x][y]
            x+=1
            y-=1
        if c & 1:
            return (sum+res-mat[c//2][c//2])
        else:
            return (sum+res)
            