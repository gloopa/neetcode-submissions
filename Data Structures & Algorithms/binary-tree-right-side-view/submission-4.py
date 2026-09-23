# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue = deque([root])
        result = []
        currrent = root
        while queue:
            length = len(queue)
            for i in range(length):
                current = queue.popleft()
                if i == length - 1:
                    result.append(current.val)
                if current.left:
                    queue.append(current.left)
                if current.right:
                        queue.append(current.right)
        return result

        