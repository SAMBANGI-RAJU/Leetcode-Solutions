class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        for i in range(len(capacity)):
            capacity[i] -= rocks[i]
        capacity.sort()

        ans = 0
        for i in capacity:
            if i <= additionalRocks:
                additionalRocks -= i
                ans += 1
        return ans