# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count =0
        if root is None:
            return 0
        def dfs(node, maximum):
            nonlocal count
            if node is None:
                return 
            if node.val >= maximum:
                count+=1
            new_max = max(maximum, node.val)
            dfs(node.left, new_max)
            dfs(node.right, new_max)
        dfs(root, root.val)
        return count
            
        