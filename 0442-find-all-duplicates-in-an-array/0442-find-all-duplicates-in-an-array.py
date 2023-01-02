class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        d={}
        ans=[]
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]]=1 
            else:
                ans.append(nums[i])
        return ans