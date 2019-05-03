# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head and head.next:
            slow_ptr = head
            fast_ptr = head.next
            even_head = head.next
            
            while fast_ptr and fast_ptr.next:
                slow_ptr.next = slow_ptr.next.next
                fast_ptr.next = fast_ptr.next.next
                slow_ptr = slow_ptr.next
                fast_ptr = fast_ptr.next
                
            slow_ptr.next = even_head
            
        return head
