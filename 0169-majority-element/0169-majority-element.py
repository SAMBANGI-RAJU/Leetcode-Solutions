from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d=Counter(nums)
        maxi=-10**9
        ans=0
        for k,v in d.items():
            if v>maxi:
                ans=k
                maxi=v 
        return ans
        
        