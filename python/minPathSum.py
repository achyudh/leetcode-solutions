class Solution:
    def __init__(self):
        self.memo = dict()
        
    def getMinPath(self, pos1, pos2):
        if (pos1, pos2) not in self.memo:
            if pos1 == self.maxPos1:
                minPath = self.getMinPath(pos1, pos2 + 1)
                
            elif pos2 == self.maxPos2:
                minPath = self.getMinPath(pos1 + 1, pos2)
                
            else:
                minPath = min(self.getMinPath(pos1, pos2 + 1), self.getMinPath(pos1 + 1, pos2))
                
            self.memo[(pos1, pos2)] = self.grid[pos1][pos2] + minPath
        
        return self.memo[(pos1, pos2)]
        
    def minPathSum(self, grid: List[List[int]]) -> int:
        self.grid = grid
        self.maxPos1 = len(grid) - 1
        self.maxPos2 = len(grid[0]) - 1
        self.memo[(self.maxPos1, self.maxPos2)] = grid[self.maxPos1][self.maxPos2]
        
        return self.getMinPath(0, 0)
