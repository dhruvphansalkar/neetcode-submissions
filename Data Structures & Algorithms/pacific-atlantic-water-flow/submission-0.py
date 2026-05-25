class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        #start from the borders
        #do graph traversal to mark all cells which can be reached from pacific
        #do graph traversal to mark all cells which can be reached from atlantic
        #perform intersection on them.
        #return intersection as array

        pacificBorder = []
        atlanticBorder = []
        for i in range(len(heights)):
            pacificBorder.append((i, 0))
            atlanticBorder.append((i, len(heights[0]) - 1))
        for j in range(len(heights[0])):
            pacificBorder.append((0, j))
            atlanticBorder.append((len(heights)-1, j))
        
        pacificSet = set()
        atlanticSet = set()

        def getAllCell(i, j, prevHeight, currentSet):
            if i not in range(len(heights)) or j not in range(len(heights[0])) or (i, j) in currentSet or heights[i][j] < prevHeight:
                return
            currentSet.add((i, j))
            getAllCell(i + 1, j, heights[i][j], currentSet)
            getAllCell(i - 1, j, heights[i][j], currentSet)
            getAllCell(i, j + 1, heights[i][j], currentSet)
            getAllCell(i, j - 1, heights[i][j], currentSet)
        
        for (i, j) in pacificBorder:
            getAllCell(i, j, -1, pacificSet)
        
        for (i, j) in atlanticBorder:
            getAllCell(i, j, -1, atlanticSet)
        
        commonCells = pacificSet & atlanticSet
        return [list(t) for t in commonCells]


        
        