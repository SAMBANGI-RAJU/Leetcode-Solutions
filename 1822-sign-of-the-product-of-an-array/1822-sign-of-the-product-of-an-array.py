class Solution:
    def arraySign(self, nums: List[int]) -> int:
        x=True
        for i in nums:
            if i==0:
                return 0 
            elif i<0:
                x=not x 
        if x:
            return 1 
        return -1