class Solution:
    def minimumTime(self, time: List[int], total: int) -> int:
        h=max(time)*total
        l=1
        while h>=l:
            m=(h+l)//2
            t=0
            for i in time:
                t+=(m//i)
            if t>=total:
                h=m-1
            else:
                l=m+1
        
        return l