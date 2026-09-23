# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True 
        
        def dfs(node):
            if not node:
                return 0
            leftd = dfs(node.left)
            rightd = dfs(node.right)
            if abs(rightd-leftd) > 1 or rightd == -1 or leftd == -1:
                return -1 
            return max(rightd, leftd) + 1
        if dfs(root) == -1:
            return False
        else:
            return True
        