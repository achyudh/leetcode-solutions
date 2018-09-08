# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result, result_head = None, None
        carry = 0
        while l1 is not None and l2 is not None:
            digit_sum = l1.val + l2.val + carry
            list_node = ListNode(digit_sum % 10)
            if result is not None:
                result.next = list_node
                result = result.next
            else:
                result = list_node
                result_head = result
            carry = digit_sum // 10
            l1 = l1.next
            l2 = l2.next
            
        while l1 is not None:
            digit_sum = l1.val + carry
            list_node = ListNode(digit_sum % 10)
            result.next = list_node
            result = result.next
            carry = digit_sum // 10
            l1 = l1.next
        
        while l2 is not None:
            digit_sum = l2.val + carry
            list_node = ListNode(digit_sum % 10)
            result.next = list_node
            result = result.next
            carry = digit_sum // 10
            l2 = l2.next
        
        if carry != 0:
            list_node = ListNode(carry)
            result.next = list_node
        
        return result_head
