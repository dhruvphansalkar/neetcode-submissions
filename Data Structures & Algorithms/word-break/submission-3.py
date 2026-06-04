class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # in the recurive solution:
        # if at len of s return true
        # iterate from i+1 to the remaining string
        # if substring is in wordDict we have 2 options
        # take the word and start recursive call
        # keep going
        # return or from the result

        words = set(wordDict)
        seen = dict()

        def recur(i: int) -> int:
            if i in seen:
                return seen[i]
            if i == len(s):
                return True
            canReachEnd = False
            for j in range(i+1, len(s) + 1):
                if s[i:j] in words:
                    canReachEnd = canReachEnd or recur(j)
            seen[i] = canReachEnd
            return seen[i]
        
        return recur(0)