class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        sol = []
        def recur(i, curr, colSeen, diagPosSeen, diagNegSeen):
            if i == n:
                sol.append(curr[:])
                return
            row = ['.'] * n
            for j in range(len(row)):
                if j not in colSeen and i - j not in diagNegSeen and i + j not in diagPosSeen:
                    row[j] = 'Q'
                    colSeen.add(j)
                    diagNegSeen.add(i-j)
                    diagPosSeen.add(i+j)
                    curr.append(''.join(row))
                    recur(i+1, curr, colSeen, diagPosSeen, diagNegSeen)
                    curr.pop()
                    colSeen.remove(j)
                    diagNegSeen.remove(i-j)
                    diagPosSeen.remove(i+j)
                    row[j] = '.'
        recur(0, [], set(), set(), set())
        return sol
            




        