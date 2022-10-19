class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        n=len(pref)
        cnt=0 
        for i in words:
            if i[:n]==pref:
                cnt+=1 
        return cnt
        