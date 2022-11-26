class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        n=len(nums)
        nums.sort()
        for i in range(n-1):
            l=i+1 
            r=n-1
            while l<r:
                if nums[i]+nums[l]+nums[r]==0:
                    res.append((nums[i],nums[l],nums[r]))
                    l+=1 
                    r-=1 
                elif nums[i]+nums[l]+nums[r]<0:
                    l+=1 
                else:
                    r-=1 
        return set(res)