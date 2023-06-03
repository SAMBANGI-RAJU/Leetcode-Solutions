class Solution:
    def setZeroes(self, a: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows=[1]*len(a)
        cols=[1]*len(a[0])
        for i in range(len(a)):
            for j in range(len(a[0])):
                if a[i][j]==0:
                    rows[i]=0 
                    cols[j]=0 
        print(rows,cols)
        for i in range(len(rows)):
            for j in range(len(cols)):
                if rows[i]==0 or cols[j]==0:
                    a[i][j]=0 
        
        