# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def tracePath(curr, target, path):
            if curr == target:
                path.append(curr)
                return True
            if not curr:
                return False
            targetOnPath = tracePath(curr.left, target, path) or tracePath(curr.right, target, path)
            if targetOnPath:
                path.append(curr)
            return targetOnPath
        
        pathP = []
        pathQ = []

        tracePath(root, p, pathP)
        tracePath(root, q, pathQ)
        pathP.reverse()
        pathQ.reverse()
        i = 0
        while i < min(len(pathP), len(pathQ)):
            if pathP[i] is not pathQ[i]:
                return pathP[i-1]
            i+=1
        if len(pathP) > len(pathQ):
            return pathQ[-1]
        else:
            return pathP[-1]

            
        