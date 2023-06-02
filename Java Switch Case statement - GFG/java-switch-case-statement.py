#User function Template for python3
import math 
class Solution:
    def switchCase(self, choice, a):
        if choice == 1:
            r = arr[0]
            area = math.pi * r * r
            return area
        elif choice == 2:
            l = arr[0]
            b = arr[1]
            area = l * b
            return area
                
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        choice = int(input())
        arr = list(map(int, input().split()))
        ob = Solution()
        if choice == 1:
            res = ob.switchCase(choice, arr)
            print(res)
        else:
            res = ob.switchCase(choice, arr)
            print(int(res))

# } Driver Code Ends