class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        res=""
        cnt=0
        maxi=0
        alpha="abcdefghijklmnopqrstuvwxyz"
        for i in range(len(s)):
            res+=s[i]
            if res in alpha:
                cnt+=1
            else:
                res=s[i]
                maxi=max(cnt,maxi)
                cnt=1
            maxi=max(cnt,maxi)
        return maxi
                