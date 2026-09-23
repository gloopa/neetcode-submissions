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
        diam = 0
        
        def dfs(node):
            if not node:
                return 0
            nonlocal diam
            left = dfs(node.left)
            right = dfs(node.right)
            diam = max(diam, (right+left))
            return max(left, right) + 1
        dfs(root)
        return diam
            
        