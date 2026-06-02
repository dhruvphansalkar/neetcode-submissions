class Solution:
    def countSubstrings(self, s: str) -> int:
        def expand(i: int, j:int) -> int:
            total = 0
            while i >= 0 and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1
                total += 1
            return total
        
        
        sol = 0
        for i in range(len(s)):
            even = expand(i, i+1)
            odd = expand(i, i)
            sol += (even + odd)
        return sol
        