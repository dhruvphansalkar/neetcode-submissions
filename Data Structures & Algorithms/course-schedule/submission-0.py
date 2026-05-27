class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        #this is topological sort.
        #create adjacency graph where for each element in the prereq array, create a entry in a map so that map[prereq] = [course]
        #run a dfs on it, with 2 sets. One for seen and one for onStack
        #if element in on Stack means there is a loop. return false

        #topological sort reverse of postOrder traversal, can this be used?
        graph = {i: [] for i in range(numCourses)}
        for curr, pre in prerequisites:
            graph[pre].append(curr)

        seen = set()
        def isLoopPresent(curr: int, stack: set) -> bool:
            if curr in stack:
                return True
            if curr in seen:
                return False
            stack.add(curr)
            for nxt in graph[curr]:
                if isLoopPresent(nxt, stack):
                    return True
            stack.remove(curr)
            seen.add(curr)
            return False

        
        for i in range(numCourses):
            if isLoopPresent(i, set()):
                return False
        return True
        

        