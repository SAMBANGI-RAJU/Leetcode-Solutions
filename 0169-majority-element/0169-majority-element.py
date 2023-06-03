from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # a=Counter(nums)
        # """a={}
        # for i in range(len(nums)):
        #     if nums[i] not in a:
        #         a[nums[i]]=1
        #     else:
        #         a[nums[i]]+=1 
        # re=max(a.values())"""
        # temp=0
        # for k,v in a.items():
        #     if v>temp:
        #         res=k 
        #         temp=v 
        # return res
        return sorted(nums)[len(nums)//2]