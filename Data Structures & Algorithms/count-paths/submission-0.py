class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[[-1]*n for _ in range(m)]
        dp[0][0]=1

        def cache(i,j):
            if i<0 or i>=m or j<0 or j>=n:
                return 0
            else:
                return dp[i][j] 
        for i in range(m):
            for j in range(n):
                if dp[i][j]==-1:
                    dp[i][j]=cache(i-1,j)+cache(i,j-1)
        return dp[m-1][n-1]
