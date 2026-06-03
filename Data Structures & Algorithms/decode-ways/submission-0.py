class Solution:
    def numDecodings(self, s: str) -> int:
        # input is a string of numbers
        # at every index i either resolve it and go next
        # or resolve it and the next and jump 2 indexes if it can be resolved
        # return 0 if we reach end on string

        allowed = set()
        for i in range(1, 27):
            allowed.add(str(i))

        # dp solution which converts recursive solution to array lookup
        dp = [0] * (len(s) + 1)
        dp[-1] = 1
        for i in range(len(s)-1, -1, -1):
            resolve1 = 0
            resolve2 = 0
            if s[i] in allowed:
                resolve1 = dp[i + 1]
            if i + 2 <= len(s) and s[i:i+2] in allowed:
                resolve2 = dp[i + 2]
            dp[i] = resolve1 + resolve2
        return dp[0]

        #recursice solution not memoising it since that is trivial, use dictionary
        def recur(i: int) -> int:
            if i == len(s):
                return 1
            if i > len(s):
                return 0
            resolve1 = 0
            resolve2 = 0
            if s[i] in allowed:
                resolve1 = recur(i + 1)
            if i+2 <= len(s) and s[i: i+2] in allowed:
                resolve2 = recur(i + 2)
            return resolve1 + resolve2
        return recur(0)
            
            

                
        