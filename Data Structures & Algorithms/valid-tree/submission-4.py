class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #conditions for a valid tree
        # should be connected
        # should not have cycles.
        # for a connected undirected graph to not have cycles the number of edges will alwas be equal to no of nodes -1
        # can be done with union find or dfs
        if (n-1) != len(edges):
            return False
        
        graph = UnionFind(n)
        for n1, n2 in edges:
            if (not graph.union(n1, n2)):
                return False
        
        return True
    
class UnionFind:
    def __init__(self, noOfNodes: int):
        self.noOfNodes = noOfNodes
        self.parent = [i for i in range(noOfNodes)]
        self.power = [1] * noOfNodes

    def find(self, curr):
        if self.parent[curr] != curr:
            self.parent[curr] = self.find(self.parent[curr])
        return self.parent[curr]

    def union(self, node1: int, node2: int) -> bool:
        parent1 = self.find(node1)
        parent2 = self.find(node2)
        if parent1 == parent2:
            return False

        if self.power[parent1] < self.power[parent2]:
            self.parent[parent1] = parent2
            self.power[parent2] += self.power[parent1]
        else:
            self.parent[parent2] = parent1
            self.power[parent1] += self.power[parent2]
        return True

    
    



        