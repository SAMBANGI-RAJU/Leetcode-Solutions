class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        while len(stones)>1:
            stones[-2]=stones[-1]-stones[-2]
            stones=stones[:-1]
            stones.sort()
            #print(stones)
        return stones[-1]