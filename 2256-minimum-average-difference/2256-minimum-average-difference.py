class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        left=0 
        right=sum(nums)
        N=len(nums)
        mini=10**20
        res=0
        minindex=0
        for i in range(N):
            left+=nums[i]
            right-=nums[i]
            if i+1==N:
                res=abs(left//(i+1))
            else:
                
                res= abs(left//(i+1)-right//(N-i-1))
            if res<mini:
                mini=res
                minindex=i
        return minindex