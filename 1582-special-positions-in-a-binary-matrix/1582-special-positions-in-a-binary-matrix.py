class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        ans=0
        transposemat=list(zip(*mat))
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j]==1 and sum(mat[i])==1 and sum(transposemat[j])==1:
                    ans+=1 
        return ans
    

                