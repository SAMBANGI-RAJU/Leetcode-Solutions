class Solution:
    def largestOddNumber(self, num: str) -> str:
        for i in range(len(num)-1,-1,-1):
            if int(num[i]) & 1:
                idx = i
                return str(num[:idx+1])
        return ""