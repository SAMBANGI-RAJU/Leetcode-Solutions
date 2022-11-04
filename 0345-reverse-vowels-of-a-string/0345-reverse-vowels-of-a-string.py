class Solution:
    def reverseVowels(self, s: str) -> str:
        l=[]
        res=""
        for i in s:
            if i in "aeiouAEIOU":
                l.append(i)
        for i in s:
            if i in "aeiouAEIOU":
                res+=l.pop()
            else:
                res+=i 
        return res
        