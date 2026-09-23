# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        current = root
        queue = []
        result = [] #hold all the values
        queue.append(root)
        while len(queue) > 0:
            current_level = []
            level_length = len(queue)
            for i in range(level_length):
                current = queue.pop(0)
                current_level.append(current.val)
                if current.left is not None:
                    queue.append(current.left)
                if current.right is not None:
                    queue.append(current.right)
            result.append(current_level)
        return result


        