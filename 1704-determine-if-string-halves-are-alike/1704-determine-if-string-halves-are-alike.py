from collections import Counter
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n=len(s)
        vow=['a','A','e','E','i','I','o','O','u','U']
        a=[s[i] for i in range(n//2) if s[i] in vow]
        b=[s[i] for i in range(n//2,n) if s[i] in vow]
        return len(a)==len(b)
        
        
        