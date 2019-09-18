# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def parseNextVal(self, index):    
        prevIndex = index
        while index < len(self.s) and self.s[index] != '-':
            index += 1
        return int(self.s[prevIndex:index]), index
    
    def parseNextDepth(self, index):
        prevIndex = index
        while self.s[index] == '-':
            index += 1
        return index - prevIndex, index
        
    def recoverFromPreorder(self, s: str) -> TreeNode:
        self.s = s
        nextVal, index = self.parseNextVal(0)
        rootNode = TreeNode(nextVal)
        stack = [rootNode]
        depth = 0
        
        while index < len(s):
            nextDepth, index = self.parseNextDepth(index)
            nextVal, index = self.parseNextVal(index)
            nextNode = TreeNode(nextVal)
            
            if nextDepth <= depth:
                for _ in range(depth - nextDepth + 1):
                    stack.pop()
                stack[-1].right = nextNode
                
            else:
                stack[-1].left = nextNode
            
            stack.append(nextNode)
            depth = nextDepth
            
        return rootNode
