class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        l=[-1]*n
        for i in edges:
            p,c=i
            if l[c]==-1:
                l[c]=p
            else:
                l[p]=c
        for h in range(n-1,-1,-1):
            if hasApple[h] and l[h]!=-1:
                hasApple[l[h]]=True
        return sum(hasApple[1:])*2