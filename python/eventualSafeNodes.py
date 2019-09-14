class Solution: 
    def __init__(self):
        self.safeNodes = dict()
        
    def isSafeNode(self, currentNode):
        if currentNode in self.safeNodes:
            return self.safeNodes[currentNode]
        
        elif not self.graph[currentNode]:
            self.safeNodes[currentNode] = True
            return True
        
        elif currentNode in self.visitedNodes:
            self.safeNodes[currentNode] = False
            return False
        
        else:    
            self.visitedNodes.add(currentNode)
            
            for nextNode in self.graph[currentNode]:
                if not self.isSafeNode(nextNode):
                    self.safeNodes[currentNode] = False
                    return False

            self.safeNodes[currentNode] = True
            return True
    
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        self.graph = graph
        
        for i0 in range(len(graph)):
            self.visitedNodes = set()
            self.isSafeNode(i0)
        
        return sorted([k for k, v in self.safeNodes.items() if v])
