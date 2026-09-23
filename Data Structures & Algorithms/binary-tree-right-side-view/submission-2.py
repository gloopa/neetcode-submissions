# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #BFS to get each level, and return the last node in each level, as that is not blocked by any node
        if root is None:
            return []
        queue = []
        result = []
        curr = root
        queue.append(root)
        while queue:
            length = len(queue)
            for i in range(length):
                current = queue.pop(0)
                if i == length - 1: #last elelmenet in each level
                    result.append(current.val)
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)

        return result        