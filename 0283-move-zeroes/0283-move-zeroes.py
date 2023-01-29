class Solution:
    def moveZeroes(self,a: List[int]) -> None:
        n=len(a)
        count=0
        for i in range(n):
            if a[i]!=0:
                a[count]=a[i]
                count+=1 
        #print(a)
        for i in range(count,n):
            a[i]=0 
        