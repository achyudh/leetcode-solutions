# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []
from collections import deque

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node   
    def cloneGraph(self, node):
        if node is None:
            return None
        
        cloneNodes = dict()
        dfsQueue = [node]
        
        while dfsQueue:
            current = dfsQueue.pop()
            if current is not None and current not in cloneNodes:
                cloneNode = UndirectedGraphNode(current.label)
                cloneNodes[current] = cloneNode
                
                for neighbor in current.neighbors:
                    if neighbor is not None:
                        dfsQueue.append(neighbor)

        dfsQueue = [node]
        visitedNodes = set()
        
        while dfsQueue:
            current = dfsQueue.pop()
            if current is not None and current not in visitedNodes:
                visitedNodes.add(current)
                cloneNode = cloneNodes[current]
                for neighbor in current.neighbors:
                    cloneNode.neighbors.append(cloneNodes[neighbor])
                for neighbor in current.neighbors:
                    if neighbor is not None:
                        dfsQueue.append(neighbor)
            
        return cloneNodes[node]
