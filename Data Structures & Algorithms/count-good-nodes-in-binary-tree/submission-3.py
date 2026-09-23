# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return none
        good = 0
        def dfs(node, num):
            nonlocal good
            if not node:
                return 
            if node.val >= num:
                good+=1
            new_num = max(node.val, num)
            dfs(node.left, new_num)
            dfs(node.right, new_num)
        dfs(root, root.val)
        return good
                
        