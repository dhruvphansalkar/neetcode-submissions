class Solution:
    def solve(self, board: List[List[str]]) -> None:
        seen = set()

        def markNonLandLocked0(i, j):
            if i not in range(len(board)) or j not in range(len(board[0])) or (i, j) in seen or board[i][j] == 'X':
                return
            seen.add((i, j))
            markNonLandLocked0(i+1, j)
            markNonLandLocked0(i-1, j)
            markNonLandLocked0(i, j+1)
            markNonLandLocked0(i, j-1)
        
        for i in range(len(board)):
            markNonLandLocked0(i, 0)
            markNonLandLocked0(i, len(board[0]) - 1)
        for j in range(len(board[0])):
            markNonLandLocked0(0, j)
            markNonLandLocked0(len(board) - 1, j)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if (i, j) not in seen:
                    board[i][j] = 'X'