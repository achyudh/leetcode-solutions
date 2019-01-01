class Solution:
    def __init__(self):
        self.memoized = {2: 2, 1: 1}
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n not in self.memoized:
            self.memoized[n] = self.climbStairs(n-1) + self.climbStairs(n-2) 
        return self.memoized[n]
        
