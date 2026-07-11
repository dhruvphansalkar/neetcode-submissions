class Solution:
    def rob(self, nums: List[int]) -> int:
        d = {}
        dp = [0] * (len(nums))

        for i in range(len(nums) - 1 , -1, -1):
            d1 = dp[i + 1] if i + 1 in range(len(dp)) else 0
            d2 = nums[i] + (dp[i + 2] if i + 2 in range(len(dp)) else 0)
            dp[i] = max(d1, d2)
        
        return dp[0]

        def dfs(i):
            if d.get(i):
                return d.get(i)

            if i >= len(nums):
                return 0
            
            d1 = dfs(i + 1)
            d2 = nums[i] + dfs(i + 2)

            d[i] = max(d1, d2)
            return max(d1, d2)
        
        return dfs(0)