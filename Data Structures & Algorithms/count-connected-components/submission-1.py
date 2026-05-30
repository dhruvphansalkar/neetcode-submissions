class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        noOfConnectedComponents = n
        g = UnionFind(n)
        for n1, n2 in edges:
            if g.union(n1, n2):
                noOfConnectedComponents -= 1
        
        return noOfConnectedComponents

class UnionFind:
    def __init__(self, n):
        self.noOfNodes = n
        self.parent = [i for i in range(n)]
        self.power = [1 for i in range(n)]

    def find(self, n) -> int:
        if n != self.parent[n]:
            self.parent[n] = self.find(self.parent[n])
        return self.parent[n]

    def union(self, n1, n2) -> bool:
        p1 = self.find(n1)
        p2 = self.find(n2)

        if p1 == p2:
            return False

        if self.power[p1] < self.power[p2]:
            self.parent[p1] = p2
            self.power[p2] += self.power[p1]
        else:
            self.parent[p2] = p1
            self.power[p1] += self.power[p2]
        return True
        