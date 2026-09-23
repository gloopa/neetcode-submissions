# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#solution is breadth first search, then chaning left node with right node value at each level
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        current_node = root
        queue = []
        queue.append(root)
        if root is None:
            return None
        while len(queue) > 0: #not empty
            current_node = queue.pop(0) #get the first element
            current_node.left, current_node.right = current_node.right, current_node.left
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)
        return root
        