class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graphUf = UnionFind(len(edges))
        for n1, n2 in edges:
            if (not graphUf.union(n1, n2)):
                return [n1, n2]
        return []


class UnionFind:
    def __init__(self, noOfNodes):
        self.parent = [i for i in range(noOfNodes + 1)]
        self.power = [1 for i in range(noOfNodes + 1)]
    
    def find(self, n: int) -> int:
        if n != self.parent[n]:
            self.parent[n] = self.find(self.parent[n])
        return self.parent[n]

    def union(self, n1: int, n2: int) -> bool:
        p1 = self.find(n1)
        p2 = self.find(n2)

        if p1 == p2:
            return False
        
        if self.power[p1] < self.power[p2]:
            self.parent[p1] = p2
            self.power[p1] += self.power[p2]
        else:
            self.parent[p2] = p1
            self.power[p2] += self.power[p1]
        return True
        