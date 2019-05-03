class Solution:
    def __init__(self):
        self.num_paths = {(1, 1): 1}
        
    def pathFinder(self, i, j):
        if (i, j) not in self.num_paths:
            if i == 1:
                self.num_paths[(i, j)] = self.pathFinder(i, j - 1)
            elif j == 1:
                self.num_paths[(i, j)] = self.pathFinder(i - 1, j)
            else:
                self.num_paths[(i, j)] = self.pathFinder(i, j - 1) + self.pathFinder(i - 1, j)
        return self.num_paths[(i, j)]
            
    def uniquePaths(self, m: int, n: int) -> int:
        self.pathFinder(m, n)
        return self.num_paths[(m, n)]
