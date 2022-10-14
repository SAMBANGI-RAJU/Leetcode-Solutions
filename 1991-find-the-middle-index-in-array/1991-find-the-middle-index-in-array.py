class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        totalsum=sum(nums) 
        leftsum=0
        for i in range(len(nums)):
            rightsum=totalsum-nums[i]-leftsum 
            if rightsum==leftsum:
                return i 
            leftsum+=nums[i]
        return -1
        