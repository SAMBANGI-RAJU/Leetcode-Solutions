class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi=- 10**20
        sum=0 
        for i in nums:
            sum+=i 
            maxi=max(sum,maxi)
            if sum<0:
                sum=0 
            #maxi=max(sum,maxi)
        return maxi