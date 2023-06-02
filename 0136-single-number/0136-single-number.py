from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """a=Counter(nums)
        for i in a:
            if nums.count(i)==1:
                return i"""
        val=0 
        for i in nums:
            val^=i
        return val