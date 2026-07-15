class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        seen = set()
        def dfs(i, j, k):
            if k == len(word):
                return True
            if (not (0 <= i < len(board) and 0 <= j < len(board[0]))) or (i, j) in seen or board[i][j] != word[k]:
                return False
            seen.add((i, j))
            found = dfs(i+1, j, k+1) or dfs(i, j+1, k+1) or dfs(i-1, j, k+1) or dfs(i, j-1, k+1)
            seen.remove((i, j))
            return found
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0):
                    return True
        return False
        