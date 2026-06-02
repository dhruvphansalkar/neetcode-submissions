class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(i: int, j:int) -> str:
            while i >= 0 and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1
            return s[i+1: j]
        
        
        sol = ''
        for i in range(len(s)):
            even = expand(i, i+1)
            odd = expand(i, i)
            if len(even) > len(sol):
                sol = even
            if len(odd) > len(sol):
                sol = odd
        return sol
        