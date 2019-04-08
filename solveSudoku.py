class Solution:
    def __init__(self):
        self.nums = [str(x) for x in range(1, 10)]
    
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
    
    def solveCell(self, i0, j0):
        if j0 == 9 and i0 == 8:
            return True
        elif j0 == 9:
            return self.solveCell(i0 + 1, 0)
        elif self.board[i0][j0] != '.':
            return self.solveCell(i0, j0 + 1)
        else:
            for num in self.nums:
                self.board[i0][j0] = num
                bi, bj = i0 // 3, j0 // 3
                if self.isValidBlock(bi, bj) and self.isValidRow(i0) and self.isValidColumn(j0):
                    if self.solveCell(i0, j0 + 1):
                        return True
            self.board[i0][j0] = '.'  
            return False
    
    def solveSudoku(self, board: List[List[str]]) -> None:
        self.board = board
        self.solveCell(0, 0)
