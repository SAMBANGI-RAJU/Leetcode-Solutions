def f(ind1,ind2,s1,s2,dp):
	if(ind1 == 0 or ind2 == 0):
		return 0
	
	if(dp[ind1][ind2] != -1):
		return dp[ind1][ind2]
	
	if(s1[ind1-1] == s2[ind2-1]):
		dp[ind1][ind2] = 1 + f(ind1-1,ind2-1,s1,s2,dp)
		return dp[ind1][ind2]
	
	dp[ind1][ind2] = max(f(ind1-1,ind2,s1,s2,dp),f(ind1,ind2-1,s1,s2,dp))
	return dp[ind1][ind2]

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        dp = [[-1 for i in range(m+1)] for i in range(n+1)]
        return f(n,m,text1,text2,dp)