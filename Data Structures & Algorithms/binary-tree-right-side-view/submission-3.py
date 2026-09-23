# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #bfs, and get the last element as that is the right most 
        if not root:
            return []
        current = root
        queue = []
        result = []
        queue.append(root)
        while queue:
            level_length = len(queue) # holds the length of each level's nodes
            for i in range(level_length):
                current = queue.pop(0)
                if i == level_length - 1: #if current node is the last element via i
                    result.append(current.val)
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
        return result
        