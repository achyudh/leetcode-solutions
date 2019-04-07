# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        heap = list()
        m_list = list()
        
        for i0 in range(len(lists)):
            if lists[i0]:
                heapq.heappush(heap, (lists[i0].val, i0))
                lists[i0] = lists[i0].next
        
        while heap:
            val, i0 = heapq.heappop(heap)
            m_list.append(val)
            if lists[i0]:
                heapq.heappush(heap, (lists[i0].val, i0))
                lists[i0] = lists[i0].next
            
        return m_list
