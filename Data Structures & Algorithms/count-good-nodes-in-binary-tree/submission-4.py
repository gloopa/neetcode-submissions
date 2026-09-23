# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good = 0
        if not root:
            return 0
        def dfs(node, value):
            nonlocal good
            if not node:
                return
            if node.val >= value:
                good += 1
            new_max = max(node.val, value)
            dfs(node.left, new_max)
            dfs(node.right, new_max)
        dfs(root, root.val)
        return good

        