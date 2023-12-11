from collections import Counter
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        dic = defaultdict(int)
        for i in arr:
            dic[i] += 1
            if dic[i] > 0.25*len(arr):
                return i