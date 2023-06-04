from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        d=Counter(s)
        res=sorted(d,key=d.get,reverse=True)
        x=""
        #print(d[res[0]])
        for i in range(len(res)):
            x+=(res[i]*d[res[i]])
        return x