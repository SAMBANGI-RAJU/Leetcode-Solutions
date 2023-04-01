class Solution:
    def search(self, a: List[int], target: int) -> int:
        if len(a)<2:
            if a[0]==target:
                return 0
        i,j=0,len(a)
        while i<j:
            mid=(i+j)//2 
            if a[mid]==target:
                return mid
            elif a[mid]>target:
                j-=1 
            else:
                i+=1 
        return -1
