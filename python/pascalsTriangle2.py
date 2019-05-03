class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]
        else:
            triangle = [1, 1]
            for i0 in range(1, rowIndex + 1):
                temp = [1 for x in range(i0 + 1)]
                for i1 in range(1, i0):
                    temp[i1] = triangle[i1-1] + triangle[i1]
                triangle = temp
            return triangle
