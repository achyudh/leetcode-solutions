class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ylen = len(matrix)
        xlen = len(matrix[0])
        zero_row = False
        zero_col = False
        
        for i0 in range(0, ylen):
            if matrix[i0][0] == 0:
                zero_col = True
                break
                
        for j0 in range(0, xlen):
            if matrix[0][j0] == 0:
                zero_row = True
                break
        
        for i0 in range(1, ylen):
            for j0 in range(1, xlen):
                if matrix[i0][j0] == 0:
                    matrix[i0][0] = 0
                    matrix[0][j0] = 0
                    
        for i0 in range(ylen - 1, 0, -1):
            if matrix[i0][0] == 0:
                for j0 in range(xlen - 1, 0, -1):
                    matrix[i0][j0] = 0
                
        for j0 in range(xlen - 1, 0, -1):
                if matrix[0][j0] == 0:
                    for i0 in range(ylen - 1, 0, -1):
                        matrix[i0][j0] = 0
                        
        if zero_col:
            for i0 in range(0, ylen):
                matrix[i0][0] = 0
        
        if zero_row:
            for j0 in range(0, xlen):
                matrix[0][j0] = 0
