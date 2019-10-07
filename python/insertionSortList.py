# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insertNode(self, node: ListNode, index: int):
        if index:
            iter0 = self.head
            for i0 in range(index - 1):
                iter0 = iter0.next
            
            node.next = iter0.next
            iter0.next = node
            
        else:
            node.next = self.head
            self.head = node
            
    def removeNode(self, index: int):
        if index:
            iter0 = self.head
            for i0 in range(index - 1):
                iter0 = iter0.next
            
            node = iter0.next
            iter0.next = iter0.next.next
            
        else:
            node = self.head
            self.head = node.next
            
        return node
    
    def insertionSortList(self, head: ListNode) -> ListNode:
        self.head = head
        iter1 = self.head
        idx1 = 0
        
        while iter1:
            idx2 = 0
            iter2 = self.head
            node = self.removeNode(idx1)
            
            while idx1 > idx2 and iter1.val > iter2.val:
                idx2 += 1
                iter2 = iter2.next
                
            idx1 += 1
            iter1 = iter1.next
            self.insertNode(node, idx2)
                
        return self.head
