class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        sum = 0
        cumulativeSumFreq = {}

        for num in nums:
            sum += num
            if sum == k:
                count += 1
            if sum - k in cumulativeSumFreq:
                count += cumulativeSumFreq[sum - k]
            if sum in cumulativeSumFreq:
                cumulativeSumFreq[sum] += 1
            else:
                cumulativeSumFreq[sum] = 1

        return count