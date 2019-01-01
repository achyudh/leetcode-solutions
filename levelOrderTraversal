# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.traversal = list()
    
    def traverse(self, root, depth):
        if root is not None:    
            if len(self.traversal) - 1 < depth:
                self.traversal.append(list())
            self.traversal[depth].append(root.val)
            self.traverse(root.left, depth + 1)
            self.traverse(root.right, depth + 1)
        
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        self.traverse(root, 0)
        return self.traversal
