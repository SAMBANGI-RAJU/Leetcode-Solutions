class Solution:
    def maxPower(self, s: str) -> int:
        cnt=0
        maxi=0
        for i in range(1,len(s)):
            if s[i]==s[i-1]:
                cnt+=1
                maxi=max(maxi,cnt)
            else:
                cnt=0
        return maxi+1
                
            
            
        