class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        #nums.sort()
        nums.sort()
        res = []
        
        for query in queries:
            i = 0
            currentSum = 0
            while i<len(nums):
                if currentSum+nums[i] > query: break 
                currentSum+=nums[i]
                i+=1
            res.append(i)
        return res
                    