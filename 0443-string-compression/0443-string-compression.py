class Solution:
    def compress(self, chars: List[str]) -> int:
        # d={}
        # x=[]
        # for i in range(1,len(chars)):
        #     if chars[i-1]==chars[i]:
        #         x.append(chars[i-1])
        #     else:
        #         d[chars[i]]=len(x)+1
        #         x=[]
        # res=[]
        # #print(d)
        # for k,v in d.items():
        #     if v==1:
        #         res.append(k)
        #     else:
        #         res.append(k)
        #         if v>10:
        #             for i in str(v):
        #                 res.append(str(i))
        #         else:
        #             res.append(str(v))
        # chars[:]=res
        # return len(chars)
        s = []
        for key, group in groupby(chars):
            #print(key, list(group))
            count = len(list(group))
            s.append(key)
            if count > 1: 
                s.extend(list(str(count)))
        chars[:] = s