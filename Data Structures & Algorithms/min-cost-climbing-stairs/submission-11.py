class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        dp = [0] * (len(cost) + 2)
        dp[-1] = float('inf')

        for i in range(len(dp) - 3, -1, -1):
            d1 = dp[i + 1] + cost[i]
            d2 = dp[i + 2] + cost[i]
            dp[i] = min(d1, d2)
        return min(dp[0], dp[1])

        d = {}
        def dfs(step):
            if step in d:
                return d[step]
            if step == len(cost):
                return 0            
            if step > len(cost):
                return float('inf')            
            d1 = dfs(step + 1) + cost[step]
            d2 = dfs(step + 2) + cost[step]
            d[step] = min(d1, d2)
            return min(d1, d2)
        return min(dfs(0), dfs(1))

