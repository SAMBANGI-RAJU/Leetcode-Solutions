class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max = 0
        cur=0
        for x in nums:
            if x == 1:
                cur+=1
                if cur > max:
                    max = cur 
            else:
                cur = 0
                
        return max