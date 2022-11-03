from collections import Counter 
class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        c=collections.Counter(words)
        found=0
        l=0
        for w in c.keys():
            if w==w[::-1]:
                if c[w]%2==1:
                    found=2
                    
                l+=(c[w]//2*2)*2
                
            else:
                l+=min(c[w],c[w[::-1]])*2
                
        return l+found