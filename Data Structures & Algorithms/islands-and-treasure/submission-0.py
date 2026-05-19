class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        def dfs(i: int, j: int, currentDistance: int):
            if i not in range(0, len(grid)) or j not in range(0, len(grid[0])) or (grid[i][j] <= currentDistance and currentDistance != 0):
                return
            grid[i][j] = currentDistance
            dfs(i+1, j, currentDistance + 1)
            dfs(i-1, j, currentDistance + 1)
            dfs(i, j+1, currentDistance + 1)
            dfs(i, j-1, currentDistance + 1)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    dfs(i, j, 0)
                    
        