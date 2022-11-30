class Solution:
    def rotate(self, a: List[List[int]]) -> None:
        n=len(a)
        a.reverse()
        for i in range(n):
            for j in range(i,n):
                a[j][i],a[i][j]=a[i][j],a[j][i]