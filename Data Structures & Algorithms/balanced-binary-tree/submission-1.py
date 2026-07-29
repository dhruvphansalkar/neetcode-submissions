# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        sol = [True]
        def recur(curr):
            if not curr:
                return 0
            left = recur(curr.left)
            right = recur(curr.right)
            if abs(left - right) > 1:
                sol[0] = False
            return 1 + max(left, right)
        recur(root)
        return sol[0]
        