class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse=True)
        tcost=0
        for i in range(len(cost)):
            if i%3!=2:
                tcost+=cost[i]
        return tcost
            