class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        n=len(nums)
        l1=nums[:n//2]
        l2=nums[n//2:]
        #print(l1,l2)
        res=[]
        for i in range(len(l1)):
            res.append(l1[i])
            res.append(l2[i])
        return res