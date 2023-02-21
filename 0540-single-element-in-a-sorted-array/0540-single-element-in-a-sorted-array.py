from collections import Counter
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        d=Counter(nums)
        for k,v in d.items():
            if v==1:
                return k