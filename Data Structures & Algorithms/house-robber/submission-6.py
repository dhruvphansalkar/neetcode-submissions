class Solution:
    def rob(self, nums: List[int]) -> int:
        d = {}

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