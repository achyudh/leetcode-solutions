# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        elif root.left is None and root.right is None:
            return 1
        else:
            lDepth = float('inf')
            rDepth = float('inf')
            if root.left is not None:
                lDepth = self.minDepth(root.left)
            if root.right is not None:
                rDepth = self.minDepth(root.right)
            return 1 + min(lDepth, rDepth)
