class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        sm,mx = 0,0
        for i in range(len(nums)):
            sm += nums[i]
            mx = max(mx,(sm + i)//(i + 1))
        return mx