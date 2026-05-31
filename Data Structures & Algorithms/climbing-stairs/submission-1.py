class Solution:
    def climbStairs(self, n: int) -> int:

        m = {}

        def recur(i: int):
            if i == n:
                return 1
            if i > n:
                return 0
            if i in m:
                return m[i]
            m[i] = recur(i+1) + recur(i+2)
            return m[i]
        
        return recur(0)
            
        