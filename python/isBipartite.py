from collections import deque

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        colors = dict()
        
        for rootNode in range(len(graph)):
            if rootNode not in colors:
                colors[rootNode] = 0
                queue = deque()
                queue.append(rootNode)

                while queue:
                    currentNode = queue.popleft()
                    currentColor = colors[currentNode]

                    for nextNode in graph[currentNode]:
                        if nextNode in colors:
                            if currentColor == colors[nextNode]:
                                return False
                        else:
                            queue.append(nextNode)
                            colors[nextNode] = 1 - currentColor
        
        return True
