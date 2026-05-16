class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #iterte over the 2d array.
        #if see 1 increment the count and trigger dfs or bfs
            #in the bfs mark 1 as 0
        #return total count

        def dfs(i: int, j: int):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == '0':
                return
            grid[i][j] = '0'
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)  

        islandCount = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    islandCount += 1
                    dfs(i, j)
        return islandCount

        