class Solution:       
    def isValidBlock(self, bi, bj):
        numbers = set()
        for i0 in range(3 * bi, 3 * (bi + 1)):
            for j0 in range(3 * bj, 3 * (bj + 1)):
                if self.board[i0][j0] != '.': 
                    if self.board[i0][j0] in numbers:
                        return False
                    numbers.add(self.board[i0][j0])
        return True
    
    def isValidRow(self, i0):
        numbers = set()
        for j0 in range(9):
            if self.board[i0][j0] != '.': 
                if self.board[i0][j0] in numbers:
                    return False
                numbers.add(self.board[i0][j0])
        return True
    
    def isValidColumn(self, j0):
        numbers = set()
        for i0 in range(9):
            if self.board[i0][j0] != '.': 
                if self.board[i0][j0] in numbers:
                    return False
                numbers.add(self.board[i0][j0])
        return True
    
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        self.board = board
        
        for i0 in range(9):
            if not self.isValidRow(i0):
                return False
            
        for j0 in range(9):
            if not self.isValidColumn(j0):
                return False
        
        for bi in range(3):
            for bj in range(3):
                if not self.isValidBlock(bi, bj):
                    return False
                
        return True
        
