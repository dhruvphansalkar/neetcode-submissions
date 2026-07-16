class Solution:
    def partition(self, s: str) -> List[List[str]]:
        sol = []
        def isPalindrome(startIndex, endIndex):
            while startIndex < endIndex:
                if s[startIndex] != s[endIndex]:
                    return False
                startIndex += 1
                endIndex -= 1
            return True
        def recur(i, curr):
            print(curr)
            if i == len(s):
                sol.append(curr[:])
                return
            for j in range(i + 1, len(s) + 1):
                if isPalindrome(i, j-1):
                    curr.append(s[i:j])
                    print(curr)
                    recur(j, curr)
                    curr.pop()
        recur(0, [])
        return sol
        
                