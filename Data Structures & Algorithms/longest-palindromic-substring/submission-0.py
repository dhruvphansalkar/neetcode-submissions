class Solution:
    def longestPalindrome(self, s: str) -> str:
        def getEvenPalindrome(i: int, j:int) -> str:
            while i >= 0 and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1
            return s[i+1: j]
        
        def getOddPalindrome(i: int) -> str:
            j = i
            while i >= 0 and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1
            return s[i+1:j]
        
        sol = ''
        for i in range(len(s)):
            even = getEvenPalindrome(i, i+1)
            odd = getOddPalindrome(i)
            if len(even) > len(sol):
                sol = even
            if len(odd) > len(sol):
                sol = odd
        return sol
        