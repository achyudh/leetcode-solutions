class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix:
            i0, j0 = 0, len(matrix[0]) - 1
            while i0 < len(matrix) and j0 >= 0:
                if matrix[i0][j0] < target:
                    i0 += 1
                elif matrix[i0][j0] > target:
                    j0 -= 1
                else:
                    return True
        return False
            
