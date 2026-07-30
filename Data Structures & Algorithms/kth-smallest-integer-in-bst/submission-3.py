# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        sol = []
        def dfs(curr, count):
            if not curr:
                return count
            if len(sol) == 1:
                return float('inf')
            leftCount = dfs(curr.left, count)
            currentNodeCount = leftCount + 1
            if currentNodeCount == k:
                sol.append(curr.val)
                return float('inf')
            return dfs(curr.right, currentNodeCount)
        dfs(root, 0)
        return sol[0]
        