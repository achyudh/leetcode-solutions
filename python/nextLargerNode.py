# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        length = 0
        iterator = head
        
        while iterator:
            iterator = iterator.next
            length += 1
        
        stack = []
        answer = [0 for x in range(length)]
        
        index = 0
        while head:
            while stack and stack[-1][0] < head.val:
                _, i = stack.pop()
                answer[i] = head.val
                
            stack.append((head.val, index))
            head = head.next
            index += 1
        
        return answer
