from collections import Counter
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        d = Counter(arr)
        res = []
        for key,v in d.items():
            if v==1:
                res.append(key)
        if k > len(res):
            return ""
        
        return res[k-1]