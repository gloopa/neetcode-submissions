# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #dfs
        if root is None:
            return 0
        self.diameter = 0
        def dfs(node):
            if node is None:
                return 0
            left_depth = dfs(node.left)
            right_depth = dfs(node.right)
            self.diameter = max(self.diameter, right_depth + left_depth)
            return max(left_depth, right_depth) + 1
        dfs(root)
        return self.diameter
        