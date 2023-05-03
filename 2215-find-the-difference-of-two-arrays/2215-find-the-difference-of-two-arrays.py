class Solution:
    def findDifference(self, num1: List[int], num2: List[int]) -> List[List[int]]:
        res1=[]
        res2=[]
        res=[]
        for i in range(len(num1)):
            if num1[i] not in num2 and num1[i] not in res1:
                res1.append(num1[i])
        for i in range(len(num2)):
            if num2[i] not in num1 and num2[i] not in res2:
                res2.append(num2[i])
        res.append(res1)
        res.append(res2)
        return res