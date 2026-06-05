class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        #if sum is odd, cannot split into 2
        total = sum(nums)
        if total % 2 == 1:
            return False
        
        total //=2

        dp = {}
        def recur(i: int, curr: int) -> bool:
            if (i, curr) in dp:
                return dp[(i, curr)]
            if curr == total:
                return True
            if i == len(nums):
                return False
            take = recur(i + 1, curr + nums[i])
            skip = recur(i + 1, curr)
            dp[(i, curr)] = skip or take
            return dp[(i, curr)]
        return recur(0, 0)
                

        