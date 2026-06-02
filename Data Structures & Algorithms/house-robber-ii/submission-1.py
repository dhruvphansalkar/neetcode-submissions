class Solution:
    def rob(self, nums: List[int]) -> int:

        dp1 = [0] * (len(nums) + 2)
        dp2 = [0] * (len(nums) + 2)

        if len(nums) == 1:
            return nums[0]

        for i in range(len(nums)-2, -1, -1):
            dp1[i] = max(nums[i] + dp1[i+2], dp1[i+1])
        
        for i in range(len(nums) - 1, 0, -1):
            dp2[i] = max(nums[i] + dp2[i+2], dp2[i+1])
        return max(dp1[0], dp2[1])


        # def recur(i: int, lastIndex: int) -> int:
        #     if i >= lastIndex:
        #         return 0
        #     return max(nums[i] + recur(i+2, lastIndex), recur(i+1, lastIndex))
        # return max(recur(0, len(nums) - 1), recur(1, len(nums)))
    

        