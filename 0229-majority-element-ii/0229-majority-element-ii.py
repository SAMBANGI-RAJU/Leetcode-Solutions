class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n=len(nums)//3
        a=[]
        x=list(set(nums))
        for i in x:
            if(nums.count(i)>n):
                a.append(i)

        return list(set(a))