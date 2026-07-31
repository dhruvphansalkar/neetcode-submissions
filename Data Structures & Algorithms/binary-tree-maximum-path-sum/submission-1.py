# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        sol = [float('-inf')]
        def recur(curr) -> int:
            if not curr:
                return 0
            leftVal = recur(curr.left)
            rightVal = recur(curr.right)
            sol[0] = max(sol[0], curr.val, curr.val + leftVal, curr.val + rightVal, curr.val + leftVal + rightVal) 
            return max(curr.val + leftVal, curr.val + rightVal, curr.val)
        recur(root)
        return sol[0]
            
        