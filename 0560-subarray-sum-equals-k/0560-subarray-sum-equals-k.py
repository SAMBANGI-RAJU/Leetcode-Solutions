class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cnt=0
        sum=0
        diff=0
        d={0:1}
        for num in nums:
            sum+=num
            diff=sum-k
            if diff in d:
                cnt+=d[diff]
            if sum in d:
                d[sum]+=1 
            else:
                d[sum]=1
    
        return cnt