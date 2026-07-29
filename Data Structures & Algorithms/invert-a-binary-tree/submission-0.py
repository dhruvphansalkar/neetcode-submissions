# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def recur(curr):
            if curr == None:
                return
            curr.left, curr.right = curr.right, curr.left
            recur(curr.left)
            recur(curr.right)
        recur(root)
        return root

        