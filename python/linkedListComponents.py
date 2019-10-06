# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def numComponents(self, head: ListNode, g: List[int]) -> int:
        g = set(g)
        numComponents = 0
        isNewComponent = True
        
        while head:
            if head.val in g and isNewComponent:
                numComponents += 1
                isNewComponent = False
            elif head.val not in g:
                isNewComponent = True
            head = head.next
        
        return numComponents
