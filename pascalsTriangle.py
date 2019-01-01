class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        triangle = [[1]]
        if numRows == 0:
            return []
        elif numRows == 1:
            return triangle
        
        for i0 in range(1, numRows):
            triangle.append((1 for x in range(i0 + 1)))
            for i1 in range(1, i0):
                triangle[i0][i1] = triangle[i0-1][i1-1] + triangle[i0-1][i1]
        
        return triangle
            
