# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #bfs then invert 
        current = root
        queue = []
        queue.append(current)

        if root is None:
            return None
            
        while len(queue) > 0:
            current = queue.pop(0) #get rid of the last element in the queue, so we can write it in our returining array
            current.left, current.right = current.right, current.left
            if current.left is not None:
                queue.append(current.left)
            if current.right is not None:
                queue.append(current.right)
        return root

        
        