class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        sol = []
        def recur(op, cl, curr):
            if len(curr) == 2*n:
                sol.append(curr)
                return
            if op < n:
                recur(op + 1, cl, curr + '(')
            if cl < op:
                recur(op, cl + 1, curr + ')')
        recur(0, 0, '')
        return sol
        