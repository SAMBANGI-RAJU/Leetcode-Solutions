class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        counts = [0]*26
        countp = [0]*26
        res = []
        for i in p:
            countp[ord(i)-ord('a')]+=1
        start = 0
        for j in range(len(s)):
            if j<len(p):
                counts[ord(s[j])-ord('a')]+=1
            else:
                # print(start, j, counts, countp)
                if counts == countp:
                    res.append(start)
                counts[ord(s[j])-ord('a')]+=1
                counts[ord(s[start])-ord('a')]-=1
                start+=1
        if counts == countp:
            res.append(start)
        return res