class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #conditions for a valid tree
        # should be connected
        # should not have cycles.
        # for a connected undirected graph to not have cycles the number of edges will alwas be equal to no of nodes -1
        # can be done with union find or dfs

        if len(edges) != n - 1:
            return False
        
        nodesList = []
        m = {i: [] for i in range(n)}
        for n1, n2 in edges:
            m[n1].append(n2)
            m[n2].append(n1)
        seen = set()
        
        def dfs(curr: int):
            if curr in seen:
                return
            nodesList.append(curr)
            seen.add(curr)
            for nxt in m[curr]:
                dfs(nxt)
        dfs(0)
        
        return len(nodesList) == n


        