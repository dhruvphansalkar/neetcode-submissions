class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        d = {}
        for c in s:
            if c in d:
                d[c] += 1
            else:
                d[c] = 1
        
        for c in t:
            if c not in d:
                return False
            d[c] -= 1
            if d[c] == 0:
                del(d[c])
        
        return True
        