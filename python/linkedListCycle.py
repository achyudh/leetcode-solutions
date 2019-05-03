# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return False
        ptr1 = head
        ptr2 = head.next
        while ptr1 != ptr2:
            if ptr2 is None or ptr2.next is None:
                return False
            ptr2 = ptr2.next.next
            ptr1 = ptr1.next
        return True
            
