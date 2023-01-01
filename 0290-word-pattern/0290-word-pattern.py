class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        p=list(pattern)
        s=s.split()
        d={}
        if len(p)!=len(s):
            return False
        if len(set(p)) !=len(set(s)):
            return False 
        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]]=p[i]
            else:
                if d[s[i]]!=p[i]:
                    return False 
        return True
                