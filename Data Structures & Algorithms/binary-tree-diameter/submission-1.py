# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        sol = [0]
        def recur(curr):
            if not curr:
                return 0
            left = recur(curr.left)
            right = recur(curr.right)
            sol[0] = max(sol[0], left + right)
            return max(left, right) + 1
        recur(root)
        return sol[0]
        