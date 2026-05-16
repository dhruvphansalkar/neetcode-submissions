class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        #iterate over the matrix
        #if found 1, enter dfs or bfs. does not matter which since all nodes need to be visited
        #mark the visited nodes as 0
        #keep track of largest island

        largestIslandSize = 0

        def getIslandSize(i: int, j: int) -> int:
            if i not in range(0, len(grid)) or j not in range(0, len(grid[0])) or grid[i][j] == 0:
                return 0
            grid[i][j] = 0
            return 1 + getIslandSize(i+1, j) + getIslandSize(i-1, j) + getIslandSize(i, j+1) + getIslandSize(i, j-1)

        
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if grid[i][j] == 1:
                    largestIslandSize = max(largestIslandSize, getIslandSize(i, j))

        return largestIslandSize