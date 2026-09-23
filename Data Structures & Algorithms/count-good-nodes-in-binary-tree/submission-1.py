# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0
        good = 0
        def dfs(node, maximum):
            nonlocal good
            if node is None:
                return
            if node.val >= maximum:
                good += 1
            new_max = max(node.val, maximum) #keeps track of the maximum val in path
            left = dfs(node.left, new_max)
            right = dfs(node.right, new_max)
        dfs(root, root.val)
        return good


            
        


        