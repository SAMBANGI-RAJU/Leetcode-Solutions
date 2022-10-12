class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        maxi=0 
        flag=0
        for i in range(len(nums)-2):
            if nums[i]+nums[i+1]>nums[i+2] and nums[i+1]+nums[i+2]>nums[i] and nums[i]+nums[i+2] >nums[i+1]:
                flag=1
                maxi=max(maxi, nums[i]+nums[i+1]+nums[i+2])
        if flag==1:
            return maxi 
        return 0
        