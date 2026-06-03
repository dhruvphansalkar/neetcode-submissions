class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # you need to reach the target amount.
        # at every point you choose the one of the values in the array subtract and recurse
        # if you hit 0 return 0
        # if you go negetive return inf


        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for i in range(1, len(dp)):
            coinsNeeded = float('inf')
            for coin in coins:
                coinsNeeded = min(coinsNeeded, 1 + (dp[i - coin] if i - coin >= 0 else float('inf')))
            dp[i] = coinsNeeded
        return -1 if dp[amount] == float('inf') else dp[amount]


        # recursice solution
        def recur(currentAmount: int) -> int:
            if currentAmount == 0:
                return 0
            if currentAmount < 0:
                return float('inf')
            coinsNeeded = float('inf')
            for coin in coins:
                coinsNeeded = min(coinsNeeded, 1 + recur(currentAmount - coin))
            return coinsNeeded
        
        coinsNeeded = recur(amount)
        if coinsNeeded == float('inf'):
            return -1
        return coinsNeeded

        

        