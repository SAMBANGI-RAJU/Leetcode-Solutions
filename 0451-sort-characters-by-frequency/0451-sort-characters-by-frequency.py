from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        # d={}
        # for i in s:
        #     if i not in d:
        #         d[i]=1 
        #     else:
        #         d[i]+=1 
        # sorted_dict = dict(sorted(d.items(), reverse=True,key=lambda item: item[1]))
        # res=''
        # for k,v in sorted_dict.items():
        #     res+=(k*v)
        # return res
        res=''
        d=Counter(s)
        for k,v in d.most_common():
            res+=(k*v)
        return res

        
        