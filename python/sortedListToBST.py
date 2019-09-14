# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.inputList = list()
        
    def buildBST(self, lo, hi):
        if lo > hi:
            return None
        else:
            mid = (lo + hi) // 2
            currentNode = TreeNode(self.inputList[mid])
            currentNode.left = self.buildBST(lo, mid - 1)
            currentNode.right = self.buildBST(mid + 1, hi)
            return currentNode
        
        
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        # Convert linked list to array
        while head:
            self.inputList.append(head.val)
            head = head.next
        
        return self.buildBST(0, len(self.inputList) - 1)
