class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def backtracking(res,temp,nums,start):
            res.append(temp[:])
            for i in range(start,len(nums)):
                temp.append(nums[i])
                backtracking(res,temp,nums,i+1)
                temp.pop()
        
        backtracking(res,[],nums,0)
        return res
        