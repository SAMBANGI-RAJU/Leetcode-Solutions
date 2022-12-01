class Solution:
    def twoSum(self, arr: List[int], t: int) -> List[int]:
        d={}
        for i in range(len(arr)):
            if arr[i] not in d:
                d[t-arr[i]]=i 
            else:
                return [d[arr[i]],i]