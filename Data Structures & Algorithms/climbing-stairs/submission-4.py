class Solution:
    def climbStairs(self, n: int) -> int:
        d = {}
        def dfs(step: int) -> int:
            ways = d.get(step)
            if ways:
                return ways

            if step > n:
                return 0
            if step == n:
                return 1
            
            d1 = dfs(step + 1)
            d2 = dfs(step + 2)
            ways = d1 + d2
            d[step] = ways
            return ways
        
        return dfs(0)