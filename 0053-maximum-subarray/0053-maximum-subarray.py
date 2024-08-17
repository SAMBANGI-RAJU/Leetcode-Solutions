class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum=0 
        maxi=-10**20 
        for i in nums:
            sum+=i 
            maxi=max(sum,maxi)
            if sum<0:
                sum=0 
        return maxi