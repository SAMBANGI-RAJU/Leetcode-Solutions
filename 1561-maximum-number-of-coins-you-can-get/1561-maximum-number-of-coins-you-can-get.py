class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        ans = 0
        n = len(piles)

        for i in range(n // 3, n, 2):
            ans += piles[i]

        return ans