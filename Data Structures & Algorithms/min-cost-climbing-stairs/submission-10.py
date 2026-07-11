class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
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