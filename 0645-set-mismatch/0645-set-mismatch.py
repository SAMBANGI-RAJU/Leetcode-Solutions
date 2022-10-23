from collections import Counter
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        s=set(nums)
        res=[]
        d=Counter(nums)
        for i in d:
            if d[i]==2:
                res.append(i)
        setsum=sum(s)
        nums_sum=sum([i for i in range(1,len(nums)+1)])
        res.append(nums_sum-setsum)
        return res