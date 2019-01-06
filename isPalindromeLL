# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        num_elements = 0
        curr_ptr = head
        
        while curr_ptr is not None:
            num_elements += 1
            curr_ptr = curr_ptr.next
        
        curr_ptr = head
        num_iter = 0
        while num_iter < (num_elements + 1)//2:
            num_iter += 1
            curr_ptr = curr_ptr.next
        
        last_ptr = None
        while curr_ptr is not None:
            next_ptr = curr_ptr.next
            curr_ptr.next = last_ptr
            last_ptr = curr_ptr
            curr_ptr = next_ptr
        
        while last_ptr is not None:
            if head.val != last_ptr.val:
                return False
            last_ptr = last_ptr.next
            head = head.next
        return True
