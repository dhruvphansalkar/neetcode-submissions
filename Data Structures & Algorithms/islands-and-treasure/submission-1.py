class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        # def dfs(i: int, j: int, currentDistance: int):
        #     if i not in range(0, len(grid)) or j not in range(0, len(grid[0])) or (grid[i][j] <= currentDistance and currentDistance != 0):
        #         return
        #     grid[i][j] = currentDistance
        #     dfs(i+1, j, currentDistance + 1)
        #     dfs(i-1, j, currentDistance + 1)
        #     dfs(i, j+1, currentDistance + 1)
        #     dfs(i, j-1, currentDistance + 1)

        #append all the tresure points in a queue
        #start bfs process.
        #only append greater than the current value

        q = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    q.append((i, j, 0))
        while q:
            i, j, distance = q.popleft()
            if i in range(0, len(grid)) and j in range(0, len(grid[0])) and (grid[i][j] > distance or distance == 0):
                grid[i][j] = distance
                q.append((i+1, j, distance+1))
                q.append((i-1, j, distance+1))
                q.append((i, j+1, distance+1))
                q.append((i, j-1, distance+1))
            

                    
        