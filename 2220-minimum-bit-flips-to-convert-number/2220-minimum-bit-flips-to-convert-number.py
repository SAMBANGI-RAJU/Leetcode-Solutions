class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        s=bin(start)[2:].zfill(32)
        g=bin(goal)[2:].zfill(32)
        count=0
        for i in range(32):
            if s[i]!=g[i]:
                count+=1
        # print(s,g)
        return count