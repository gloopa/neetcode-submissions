# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #bfs, invert left and right
        if not root:
            return None
        current = root
        queue = deque([root])
        result = []
        while queue:
            current = queue.popleft()
            current.left, current.right = current.right, current.left #switches
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        return root


        