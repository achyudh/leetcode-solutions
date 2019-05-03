# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root):
        return self.isBalancedHelper(root)[0]
    
    def isBalancedHelper(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True, 0
        else:
            rBal, rHeight = self.isBalancedHelper(root.right)
            lBal, lHeight = self.isBalancedHelper(root.left)
            isBal = rBal and lBal and abs(lHeight - rHeight) <= 1
            return isBal, max(rHeight, lHeight) + 1
