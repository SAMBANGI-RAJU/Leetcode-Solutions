class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        res=[]
        for i in strs:
            lst=list(i)
            str1=''.join(sorted(lst))
            if str1 not in d:
                d[str1]=[i]
            else:
                d[str1].append(i)
        res.extend(d.values())
        return res