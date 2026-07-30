# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        sol = [0]
        def dfs(curr, maxOnPath):
            if not curr:
                return
            if curr.val >= maxOnPath:
                sol[0] += 1
                maxOnPath = curr.val
            dfs(curr.left, maxOnPath)
            dfs(curr.right, maxOnPath)
        dfs(root, float('-inf'))
        return sol[0]
        