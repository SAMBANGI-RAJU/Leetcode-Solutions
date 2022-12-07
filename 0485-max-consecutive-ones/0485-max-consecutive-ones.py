class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxi = 0
        cur=0
        for x in nums:
            if x:
                cur+=1
                #if cur > max:
                 #   max = cur
                maxi=max(maxi,cur)
            else:
                cur = 0
                
        return maxi