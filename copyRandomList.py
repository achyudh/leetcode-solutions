# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if head is None:
            return None
        
        orig_ptr = head
        while orig_ptr:
            dupl_ptr = RandomListNode(orig_ptr.label)
            dupl_ptr.next = orig_ptr.next
            orig_ptr.next = dupl_ptr
            orig_ptr = dupl_ptr.next

        orig_ptr = head
        while orig_ptr:
            if orig_ptr.random is not None:
                orig_ptr.next.random = orig_ptr.random.next
            else:
                orig_ptr.next.random = None
            orig_ptr = orig_ptr.next.next
        
        orig_ptr = head
        dupl_head = head.next
        while orig_ptr:
            if orig_ptr.next:
                dup_ptr = orig_ptr.next
                orig_ptr.next = orig_ptr.next.next
                if dup_ptr.next:
                    dup_ptr.next = dup_ptr.next.next
                orig_ptr = orig_ptr.next
        
        return dupl_head
