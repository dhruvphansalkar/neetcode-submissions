class Solution:
    def rob(self, nums: List[int]) -> int:
        d = {}
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
        
        start0 = dfs(0, True)
        d = {}
        start1 = dfs(1, False)
        
        return max(start0, start1)
            
