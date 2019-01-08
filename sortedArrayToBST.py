# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, nums, low, high):
        if low > high:
            return None
        elif low == high:
            return TreeNode(nums[low])
        else:
            mid = (low + high) // 2
            root = TreeNode(nums[mid])
            root.left = self.buildTree(nums, low, mid - 1)
            root.right = self.buildTree(nums, mid + 1, high)
            return root
    
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self.buildTree(nums, 0, len(nums) - 1)
