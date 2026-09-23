# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        good = 0
        def dfs(node, val):
            nonlocal good
            if not node:
                return 0
            if node.val >= val:
                good += 1
            new_max = max(node.val, val)
            left = dfs(node.left, new_max)
            right = dfs(node.right, new_max)
            return max(left, right) + 1
        dfs(root, root.val)
        return good


        