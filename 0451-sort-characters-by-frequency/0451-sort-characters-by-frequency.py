from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        d=Counter(s)
        res=sorted(d,key=d.get,reverse=True)
        x=""
        for i in res:
            y=s.count(i)
            x=x+(i*y)
        return x