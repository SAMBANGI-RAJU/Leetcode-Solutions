class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        res=[]
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]]=1 
            else:
                d[nums[i]]+=1
        res=sorted(d,key=d.get,reverse=True)
        print(res)
        return res[:k]