import math 
class Solution:
    def myPow(self, x: float, n: int) -> float:
#         if n<0:
#             return 1/x*self.myPow(x,-n)
#         if n==0:
#             return 1 
#         elif n % 2 == 0:
#             return self.myPow(x * x, n / 2)
#         # Odd Power
#         else:
#             return x * self.myPow(x, n - 1)
        if n == 0:
            return 1
        # Negative Power
        elif n < 0:
            return 1 / self.myPow(x, -n)
        # Even Power
        elif n % 2 == 0:
            return self.myPow(x * x, n / 2)
        # Odd Power
        else:
            return x * self.myPow(x, n - 1)