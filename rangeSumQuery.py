class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.cached_sums = matrix
        for i0 in range(len(matrix)):
            for j0 in range(len(matrix[i0])):
                if i0 == 0 and j0 == 0:
                    pass
                elif i0 == 0:
                    self.cached_sums[i0][j0] = self.cached_sums[i0][j0 - 1] + matrix[i0][j0]
                elif j0 == 0:
                    self.cached_sums[i0][j0] = self.cached_sums[i0 - 1][j0] + matrix[i0][j0]
                else:
                    self.cached_sums[i0][j0] = self.cached_sums[i0 - 1][j0] + self.cached_sums[i0][j0 - 1] + matrix[i0][j0] - self.cached_sums[i0 - 1][j0 - 1]     

    def sumRegion(self, row1, col1, row2, col2): 
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        if row1 == 0 and col1 == 0:
                return self.cached_sums[row2][col2]
        elif row1 == 0:
                return self.cached_sums[row2][col2] - self.cached_sums[row2][col1 - 1] 
        elif col1 == 0:
            return self.cached_sums[row2][col2] - self.cached_sums[row1 - 1][col2]
        else:
            return self.cached_sums[row2][col2] - self.cached_sums[row1 - 1][col2] - self.cached_sums[row2][col1 - 1] + self.cached_sums[row1 - 1][col1 - 1]
