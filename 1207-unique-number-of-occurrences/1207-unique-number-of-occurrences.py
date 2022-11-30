from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        b=Counter(arr)
        res=[]
        for k,v in b.items():
            res.append(v)
        res_list=list(set(res))
        return len(res_list)==len(res)
            
        
        