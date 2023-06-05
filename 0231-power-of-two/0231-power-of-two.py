import math
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        cnt=0 
        temp=n
        while n>0:
            n= n & (n-1)
            cnt+=1 
        return cnt==1 and temp >0