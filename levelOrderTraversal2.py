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
        if len(self.traversal) - 1 < depth:
            self.traversal.append(list())
        self.traversal[depth].append(root.val)
        if root.left is not None:
            self.traverse(root.left, depth + 1)
        if root.right is not None:
            self.traverse(root.right, depth + 1)

    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is not None:
            self.traverse(root, 0)
        return self.traversal[::-1]
        
