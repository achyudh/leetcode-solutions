# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findPaths(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if root is None:
            return False, []
        elif root.left is None and root.right is None:
            if root.val - sum == 0:
                return True, [[root.val]]
            else:
                return False, []
        else:
            lStatus, lPath = self.findPaths(root.left, sum-root.val)
            rStatus, rPath = self.findPaths(root.right, sum-root.val)
            if lStatus:
                for path in lPath:
                    path.append(root.val)
            if rStatus:
                for path in rPath:
                    path.append(root.val)
            return lStatus or rStatus, lPath + rPath
            
    def pathSum(self, root, sum):
        if root is None:
            return []
        else:
            paths = self.findPaths(root, sum)[1]
            for i in range(len(paths)):
                paths[i] = paths[i][::-1]
            return paths
