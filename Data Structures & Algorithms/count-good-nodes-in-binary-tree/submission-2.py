# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        
        if not root:
            return 0
        
        def dfs(node, length):
            nonlocal count
            if not node:
                return 0
            if node.val >= length:
                count+=1
            new_max = max(node.val, length)
            dfs(node.left, new_max)
            dfs(node.right,new_max)
        dfs(root, root.val)
        return count