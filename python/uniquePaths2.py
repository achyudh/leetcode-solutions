class Solution:
    def __init__(self):
        self.memo = dict()
        
    def getNumPaths(self, pos1, pos2):
        if pos1 > self.maxPos1 or pos2 > self.maxPos2 or self.obstacleGrid[pos1][pos2] == 1:
            return 0
        
        elif (pos1, pos2) not in self.memo:
            self.memo[(pos1, pos2)] = self.getNumPaths(pos1 + 1, pos2) + self.getNumPaths(pos1, pos2 + 1)
            
        return self.memo[(pos1, pos2)]
    
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        self.obstacleGrid = obstacleGrid
        self.maxPos1 = len(obstacleGrid) - 1
        self.maxPos2 = len(obstacleGrid[0]) - 1
        self.memo[(self.maxPos1, self.maxPos2)] = 1
        
        return self.getNumPaths(0, 0)
    
