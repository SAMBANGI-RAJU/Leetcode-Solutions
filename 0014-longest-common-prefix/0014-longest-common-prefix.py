class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res=""
        for i in range(len(strs[0])):
            for k in strs:
                if i==len(k) or k[i]!=strs[0][i]:
                    return res
            res+=strs[0][i]
        return res