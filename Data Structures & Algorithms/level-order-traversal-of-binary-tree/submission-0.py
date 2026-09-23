# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #breadth first search -> level order
        if root is None: 
            return [] 
        current = root
        queue = []
        result = [] #hold the inner lists of diff levels' nodes
        queue.append(root) #hold the parent of the tree
        while len(queue) > 0:
            current_level  = [] #hold elements for each level in bt
            level_length = len(queue) #len of queue is how many elements are there in the level(ie: if 2 and 5, thats 2)
            for i in range(level_length):
                current = queue.pop(0)
                current_level.append(current.val) #add the value of the node in each respective level
                if current.left is not None:
                    queue.append(current.left)
                if current.right is not None:
                    queue.append(current.right)
            result.append(current_level) #add each level's elements, grouped together
        
        return result
   
        