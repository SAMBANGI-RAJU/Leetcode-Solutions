class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        parr=[]
        narr=[]
        for i in nums:
            if i>0:
                parr.append(i)
            else:
                narr.append(i)
        res=[]
        c=0
        p=0
        for i in range(len(nums)):
            if i % 2==0:
                res.append(parr[c])
                c+=1 
            else:
                res.append(narr[p])
                p+=1 
        return res
        