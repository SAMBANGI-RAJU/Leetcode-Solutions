class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        cnt=0 
        maxi=0
        for i in nums:
            if i==0:
                cnt+=1
                maxi+=cnt 
                #print(maxi)
            else:
                cnt=0
        return maxi