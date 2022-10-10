class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        size = len(s)
        max_len = 0
        start = 0
        end = 0
        for i in range(size):
            while s[i] in s[start:end]:
                start+=1    
            end+=1
            
            max_len = max(max_len, (end-start))
        return max_len