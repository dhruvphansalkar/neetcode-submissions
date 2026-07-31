# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        inOrderArray = []
        def getInorder(curr):
            if not curr:
                inOrderArray.append('N')
                return
            inOrderArray.append(str(curr.val))
            getInorder(curr.left)
            getInorder(curr.right)
        getInorder(root)
        return ','.join(inOrderArray)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        print(data)
        nodeArray = data.split(',')
        index = [0]
        def dfs():
            if index[0] >= len(nodeArray) or nodeArray[index[0]] == 'N':
                return None
            newNode = TreeNode(nodeArray[index[0]])
            index[0] += 1
            newNode.left = dfs()
            index[0] += 1
            newNode.right = dfs()
            return newNode
        return dfs()

