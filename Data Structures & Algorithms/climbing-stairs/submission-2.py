class Solution:
    def climbStairs(self, n: int) -> int:

        [0, 1, 2, 3, 4]

        dp = [0] * (n+1)
        dp[-1] = 1
        for i in range(n-1, -1, -1):
            dp[i] = dp[i+1] + (dp[i+2] if i + 2 in range(len(dp)) else 0)
        return dp[0]




        m = {}

        def recur(i: int):
            if i == n:
                return 1
            if i > n:
                return 0
            if i in m:
                return m[i]
            m[i] = recur(i+1) + recur(i+2)
            return m[i]
        
        return recur(0)
            
        