from copy import deepcopy

class Solution:
    def __init__(self):
        self.completedPaths = list()
    
    def pathIterator(self, currentPath):
        if currentPath[-1] == self.destination:
            self.completedPaths.append(deepcopy(currentPath))
            
        elif self.graph[currentPath[-1]]:
            for nextNode in self.graph[currentPath[-1]]:
                currentPath.append(nextNode)
                self.pathIterator(currentPath)
                currentPath.pop()
        
    
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.graph = graph
        self.destination = len(graph) - 1
        self.pathIterator([0])
        
        return self.completedPaths
        
