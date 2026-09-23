# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        result = []
        def dfs(node):
            if not node:
                return 
            dfs(node.left)
            result.append(node.val)
            dfs(node.right)
        dfs(root)
        left = 0
        while left < len(result) - 1:
            if result[left] >= result[left+1]:
                return False
            left+=1
        return True
        