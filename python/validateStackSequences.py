class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = list()
        pushIndex = 0
        popIndex = 0
        
        while pushIndex < len(pushed):
            stack.append(pushed[pushIndex])
            pushIndex += 1
            
            while stack and stack[-1] == popped[popIndex]:
                stack.pop()
                popIndex += 1
        
        while stack:
            nextVal = stack.pop()
            if nextVal != popped[popIndex]:
                return False
            popIndex += 1
        
        return popIndex == len(popped)
