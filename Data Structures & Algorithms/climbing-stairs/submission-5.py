class Solution:
    def climbStairs(self, n: int) -> int:

        dp = [0] * (n+1)
        dp[-1] = 1

        for i in range(len(dp) - 2, -1, -1):
            dp[i] = dp[i + 1] + (dp[i + 2] if i + 2 < len(dp) else 0)
        return dp[0]

        d = {}
        d[n] = 1
        d[n+1] = 0
        def dfs(step: int) -> int:
            if step in d:
                return d[step]
            d[step] = dfs(step + 1) +  dfs(step + 2)
            return ways
        
        return dfs(0)