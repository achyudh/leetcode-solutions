class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head and head.next:
            slow_ptr = head.next
            fast_ptr = head.next.next
            while fast_ptr and fast_ptr.next and slow_ptr != fast_ptr:
                slow_ptr = slow_ptr.next
                fast_ptr = fast_ptr.next.next
            if fast_ptr and fast_ptr.next:
                slow_ptr = head
                while slow_ptr != fast_ptr:
                    slow_ptr = slow_ptr.next
                    fast_ptr = fast_ptr.next
                return fast_ptr
        return None
