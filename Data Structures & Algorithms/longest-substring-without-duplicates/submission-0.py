class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        j = 0
        sol = 0
        for i, c in enumerate(s):
            while j < i and c in window:
                window.remove(s[j])
                j += 1
            window.add(c)
            sol = max(sol, len(window))
        return sol
            
        