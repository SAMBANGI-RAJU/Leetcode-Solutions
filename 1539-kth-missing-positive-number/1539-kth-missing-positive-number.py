class Solution:
    def findKthPositive(self, arr: List[int], k: int)-> int:
        miss=[]
        for i in range(1,arr[-1]+1):
            if i not in arr:
                miss.append(i)
        if len(miss)>=k:
            return miss[k-1]
        else:
            return arr[-1]+k-len(miss)