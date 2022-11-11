class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p = 0
        for i in nums:
            if i != nums[p]:
                p += 1
                nums[p] = i
                
        return p+1