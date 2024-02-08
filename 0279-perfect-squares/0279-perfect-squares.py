class Solution:
    def numSquares(self, n: int) -> int:
        dp = [n]*(n+1)
        dp[0]=0
        for t in range(1,n+1):
            for s in range(1,t+1):
                sq=s*s
                if t-sq<0:
                    break 
                dp[t] = min(dp[t],1+dp[t-sq])
        return dp[n]