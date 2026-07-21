class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == '':
            return []
        m = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        sol = []
        def recur(i, curr):
            if i == len(digits):
                sol.append(curr)
                return
            for c in m[digits[i]]:
                recur(i + 1, curr + c)
        recur(0, '')
        return sol

        