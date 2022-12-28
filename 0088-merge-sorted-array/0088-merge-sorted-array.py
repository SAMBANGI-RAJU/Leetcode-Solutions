class Solution:
    def merge(self, a: List[int], m: int, b: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.

        """
        if n!=0:
            a[:] = sorted(a[:-n] + b)
        
        
        