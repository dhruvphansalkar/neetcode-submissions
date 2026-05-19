"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

#dfs or bfs over the graph to create a copy for each node
#store the copy in a dictionary
#go through the map again and create a new graph with the value nodes

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if node is None:
            return node
        nodeMap = {}

        def cloneGraphRecursively(curr: Node) -> Node:
            if curr in nodeMap:
                return nodeMap[curr]
            nodeMap[curr] = Node(curr.val)
            neighborCloneArray = []
            for neighbor in curr.neighbors:
                neighborCloneArray.append(cloneGraphRecursively(neighbor))
            nodeMap[curr].neighbors = neighborCloneArray
            return nodeMap[curr]
            
        return cloneGraphRecursively(node)
        
        # def cloneNode(currentNode: Node) -> None:
        #     if currentNode in nodeMap:
        #         return
        #     copyNode = Node(currentNode.val, None)
        #     nodeMap[currentNode] = copyNode
        #     for neighbor in currentNode.neighbors:
        #         cloneNode(neighbor)
        # cloneNode(node)

        # for (orig, clone) in  nodeMap.items():
        #     if orig.neighbors == None:
        #         clone.neighbors = None
        #     else:
        #         cloneArray = []
        #         for neighbor in orig.neighbors:
        #             cloneArray.append(nodeMap[neighbor])
        #         clone.neighbors = cloneArray
        
        # return nodeMap[node]
            



        