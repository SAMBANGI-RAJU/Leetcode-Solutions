class Solution:
    def checkIfPangram(self, s: str) -> bool:
        d={}
        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]]=1
            else:
                d[s[i]]+=1 
        #print(len(d))
        return len(d)==26
            