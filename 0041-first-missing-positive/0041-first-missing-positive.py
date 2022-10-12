class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # approach 1 works good
        d={}
        for i in range(len(nums)):
            d[nums[i]]=1
        print(d)
        i=0
        for i in range(1,len(nums)+1):
            if i not in d:
                return i
        return i+1
        #approach 2
        # it having tle which 171/173 test cases have passed 
        """maxi=max(nums)
        if maxi<=0:
            return 1
        for i in range(maxi+1):
            if i not in nums and i>0:
                return i 
        return maxi+1"""