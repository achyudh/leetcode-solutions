# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTreeHelper(self, i_lo, i_hi, p_cur):
        if i_lo <= i_hi and p_cur < len(self.inorder):
            i_mid = self.inorder[self.preorder[p_cur]]
            left, p_nxt = self.buildTreeHelper(i_lo, i_mid - 1, p_cur + 1)
            right, p_nxt = self.buildTreeHelper(i_mid + 1, i_hi, p_nxt + 1)
            node = TreeNode(self.preorder[p_cur])
            node.left = left
            node.right = right
            return node, p_nxt
        else:
            return None, p_cur - 1
    
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        self.preorder = preorder
        self.inorder = {y:x for x, y in enumerate(inorder)}
        return self.buildTreeHelper(0, len(inorder) - 1, 0)[0]
