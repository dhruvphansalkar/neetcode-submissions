class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        noOfMinutes = 0
        freshFruit = 0
        q = deque()

        #traverse the array and add all rotten oranges to to the queue
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    grid[i][j] = 1
                    q.append((i, j, 0))
                if grid[i][j] == 1:
                    freshFruit += 1
        
        #all rotten oranges are in queue with time 0
        #add the adjoining oranjes, with time as +1
        #since it is structured, oranges added before will never be added again
        #if all oranges get added, solution is the greatest value at the time of adding, othervise infinity
        while q:
            i, j, time = q.popleft()
            if i not in range(len(grid)) or j not in range(len(grid[0])) or grid[i][j] != 1:
                continue
            grid[i][j] = 2
            freshFruit -= 1
            noOfMinutes = max(noOfMinutes, time)
            q.append((i + 1, j, time + 1))
            q.append((i - 1, j, time + 1))
            q.append((i, j + 1, time + 1))
            q.append((i, j - 1, time + 1))
        
        
        return noOfMinutes if freshFruit == 0 else -1
        

            
            
            

        