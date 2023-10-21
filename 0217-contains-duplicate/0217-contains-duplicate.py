class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return not len(list(set(nums)))==len(nums)
        