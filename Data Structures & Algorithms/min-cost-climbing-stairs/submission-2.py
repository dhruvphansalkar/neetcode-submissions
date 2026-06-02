class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        dp = [0] * len(cost)
        for i in range(len(dp) - 1, -1, -1):
            option1 = cost[i] + (dp[i+1] if i+1 in range(len(dp)) else 0)
            option2 = cost[i] + (dp[i+2] if i+2 in range(len(dp)) else 0)
            dp[i] = min(option1, option2)
        return min(dp[0], dp[1])


        # def recur(i: int) -> int:
        #     if i >= len(cost):
        #         return 0
            
        #     option1 = cost[i] + recur(i + 1)
        #     option2 = cost[i] + recur(i + 2)
        #     return min(option1, option2)
        # return min(recur(0), recur(1))
        