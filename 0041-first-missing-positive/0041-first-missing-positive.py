class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # approach 1 works good
        """d={}
        for i in range(len(nums)):
            d[nums[i]]=1
        print(d)
        i=0
        for i in range(1,len(nums)+1):
            if i not in d:
                return i
        return i+1"""
        # approach 2
        m = set(nums)
        
        for i in range(1, len(nums) + 2):
            if i not in m:
                return i