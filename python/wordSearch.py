class Solution:
    def validCell(self, currentY, currentX, wordIndex) -> bool:
        return currentX >= 0 and currentY >= 0 \
            and currentY < len(self.board) \
            and currentX < len(self.board[0]) \
            and self.board[currentY][currentX] == self.word[wordIndex]
    
    def search(self, currentY, currentX, wordIndex) -> bool:        
        if wordIndex == len(self.word):
            return True
        
        result = False
        if self.validCell(currentY, currentX, wordIndex):
            currentChar = self.board[currentY][currentX]
            self.board[currentY][currentX] = '0'
            
            result = self.search(currentY + 1, currentX, wordIndex + 1) \
            or self.search(currentY - 1, currentX, wordIndex + 1) \
            or self.search(currentY, currentX + 1, wordIndex + 1) \
            or self.search(currentY, currentX - 1, wordIndex + 1)
            
            self.board[currentY][currentX] = currentChar
                    
        return result
    
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.word = word
        self.board = board
        
        for startY in range(len(board)):
            for startX in range(len(board[0])):
                self.visited = set()
                if self.search(startY, startX, 0):
                    return True
        
        return False
