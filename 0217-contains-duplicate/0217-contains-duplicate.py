class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """d={}
        flag=0
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]]=i
            else:
                flag=1
        if flag==0:
            return False
        return True"""
        l=set(nums)
        if len(l)!=len(nums):
            return True 
        return False