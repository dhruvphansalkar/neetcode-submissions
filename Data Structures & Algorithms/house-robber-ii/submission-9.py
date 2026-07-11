class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        
        dp = [0] * n
        dp1 = [0] * n

        for i in range(n - 1, 0, -1):
            d1 = dp[i + 1] if i + 1 in range(n) else 0
            d2 = nums[i] + (dp[i + 2] if i + 2 in range(n) else 0)
            
            dp[i] = max(d1, d2)
        
        for i in range(n - 2, -1, -1):
            d1 = dp1[i + 1] if i + 1 in range(n) else 0
            d2 = nums[i] + (dp1[i + 2] if i + 2 in range(n) else 0)
            
            dp1[i] = max(d1, d2)

        return max(dp[1], dp1[0])




        if len(nums) == 1:
            return nums[0]
        
        def dfs(i, robbed1st = False):
            money = d.get(i)
            if money:
                return money
            
            if robbed1st and i >= len(nums) - 1:
                return 0
            if not robbed1st and i >= len(nums):
                return 0
            
            d1 = dfs(i + 1, robbed1st)
            d2 = nums[i] + dfs(i + 2, robbed1st)

            money = max(d1, d2)
            d[i] = money
            return money
        
        d = {}
        start0 = dfs(0, True)
        d = {}
        start1 = dfs(1, False)
        
        return max(start0, start1)
            
