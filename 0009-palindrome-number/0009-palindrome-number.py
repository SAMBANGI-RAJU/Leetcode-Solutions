class Solution:
    def isPalindrome(self, x: int) -> bool:
        x=str(x)
       # y=x[::-1]
        return x==x[::-1]
    
        