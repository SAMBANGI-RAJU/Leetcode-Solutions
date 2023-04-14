class Solution:
    def ExtractNumber(self,s):
        #code here
        l=s.split(" ")
        #print(l)
        maxi=-1
        for i in l:
            if '9' not in i and i.isdigit():
                maxi=max(int(i),maxi)
        return maxi


#{ 
 # Driver Code Starts
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        S=input()
        ob=Solution()
        ans=ob.ExtractNumber(S)
        print(ans)   
# } Driver Code Ends