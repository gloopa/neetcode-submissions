# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #bfs -> get the last element in queue in each level
        if not root:
            return []
        curr = root
        queue = deque([root])
        result = []
        while queue:
            level_length = len(queue)
            for i in range(level_length):
                curr = queue.popleft()
                if i == level_length - 1: #last element in queue
                    result.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
        return result
        