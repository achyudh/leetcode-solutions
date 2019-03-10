class Solution:
    def getElement(self, matrix, index):
        return matrix[index // len(matrix[0])][index % len(matrix[0])]
    
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        
        lo, hi = 0, len(matrix) * len(matrix[0]) - 1
        
        while lo <= hi:
            mid = (lo + hi) // 2
            if self.getElement(matrix, mid) < target:
                lo = mid + 1
            elif self.getElement(matrix, mid) > target:
                hi = mid - 1
            else:
                return True
            
        return False
