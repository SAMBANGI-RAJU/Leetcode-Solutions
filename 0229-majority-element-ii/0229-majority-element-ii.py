class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        d=Counter(nums)
        res=[]
        x=len(nums)//3
        for k,v in d.items():
            if v>x:
                res.append(k)
        return res