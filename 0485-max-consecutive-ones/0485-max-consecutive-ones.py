class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxcnt = cnt = 0
        for num in nums:
            if num:
                cnt += 1
            else:
                maxcnt = max(maxcnt, cnt)
                cnt = 0
        maxcnt = max(maxcnt, cnt)
        return maxcnt