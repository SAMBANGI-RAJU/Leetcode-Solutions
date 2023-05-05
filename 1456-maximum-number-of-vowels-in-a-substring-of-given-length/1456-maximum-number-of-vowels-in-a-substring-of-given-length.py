class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        cnt=0 
        j=0
        maxi=0
        for i in range(len(s)):
            if s[i] in 'aeiou':
                cnt+=1 
            if i-j+1==k:
                maxi=max(maxi,cnt)
                if s[j] in 'aeiou':
                    cnt-=1 
                j+=1 
        return maxi
                
        