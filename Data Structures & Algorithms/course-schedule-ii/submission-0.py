class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        m = {i: [] for i in range(numCourses)}
        for curr, pre in prerequisites:
            m[pre].append(curr)

        sol = []
        seen = set()

        def checkCycleAndCreateTopologicalSort(curr, stack):
            if curr in stack:
                return True
            if curr in seen:
                return False
            stack.add(curr)
            for nxt in m[curr]:
                if checkCycleAndCreateTopologicalSort(nxt, stack):
                    return True
            stack.remove(curr)
            seen.add(curr)
            sol.append(curr)
            return False
        
        for i in range(numCourses):
            if checkCycleAndCreateTopologicalSort(i, set()):
                return []
        return sol[::-1]
        