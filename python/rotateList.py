# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not (head and head.next and k):
            return head
        
        length = 1
        nodePtr = head
        while nodePtr.next:
            nodePtr = nodePtr.next
            length += 1
        
        newHead = head
        k = k % length
        
        if k:
            for _ in range(length - k - 1):
                newHead = newHead.next

            newTail = newHead
            newHead = newHead.next
            newTail.next = None

            nodePtr = newHead
            while nodePtr.next:
                nodePtr = nodePtr.next
            nodePtr.next = head
        
        return newHead
