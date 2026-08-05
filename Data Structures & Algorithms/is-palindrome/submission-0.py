class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        valid = set([chr(i) for i in range(ord('a'), ord('z') + 1)])
        for i in range(ord('0'), ord('9') + 1):
            valid.add(chr(i))
            
        i, j = 0, len(s) - 1
        while i < j:
            while i < j and s[i] not in valid:
                i += 1
            while i < j and s[j] not in valid:
                j -= 1
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
        