class Solution:
    def countAndSay(self, n: int) -> str:
        def rec(n):
            if n==1:                             
                return "1"
            temp = rec(n-1)                 
            return say(temp)
        
		
		# For this function, we are using two pointers to count the consecutive same digits.
        def say(st):
            s = list(st)

            res = ""
            i,j = 0,0
            while i<len(s):
                c = 0
                while j<len(s) and s[i]==s[j]:
                    c+=1
                    j+=1
                if c!=0:
                    res+=str(c)+str(s[i])        
                else:
                    res+=str(s[i])
                i=j
            return res
        
        return rec(n)
        