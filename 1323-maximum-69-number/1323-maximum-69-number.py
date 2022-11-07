class Solution:
    def maximum69Number (self, num: int) -> int:
        ans=list(str(num))
        maxi=num
        flag=0
        for i in range(len(ans)):
            if ans[i]=='9':
                flag=1
                ans[i]='6'
            else:
                flag=0
                ans[i]='9'
            res=int(''.join(ans))
            #print(res)
            maxi=max(maxi,res)
            if flag==0:
                ans[i]='6'
            else:
                ans[i]='9'
        return maxi
                
            
        