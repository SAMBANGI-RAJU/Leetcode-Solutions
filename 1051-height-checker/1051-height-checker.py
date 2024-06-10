class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        new_heights = sorted(heights)
        cnt = 0
        for i in range(len(heights)):
            if (new_heights[i]!=heights[i]):
                cnt+=1 
        return cnt