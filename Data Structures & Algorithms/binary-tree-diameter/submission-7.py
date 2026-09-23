# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        diameter = 0

        def dfs(node):
            nonlocal diameter
            if not node:
                return 0 
            leftd = dfs(node.left)
            rightd = dfs(node.right)
            diameter = max(diameter, rightd+leftd)
            return max(rightd, leftd) + 1
        dfs(root)
        return diameter
        