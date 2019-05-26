# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.maxValue = float('-inf')
    
    def nodePathSum(self, root: TreeNode):
        if not root:
            return 0
        
        leftSum = max(0, self.nodePathSum(root.left))
        rightSum = max(0, self.nodePathSum(root.right))
        self.maxValue = max(self.maxValue, root.val + leftSum + rightSum)
        return root.val + max(leftSum, rightSum)
    
    def maxPathSum(self, root: TreeNode) -> int:
        self.nodePathSum(root)
        return self.maxValue
