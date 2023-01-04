class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        #l=[]
        pairs=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]==nums[j] and i<j :
                    #l.append((nums[i],nums[j]))
                    pairs+=1 
        return pairs