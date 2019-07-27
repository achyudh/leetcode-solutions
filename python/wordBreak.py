class Solution:
    def __init__(self):
        self.memo = dict()
        
    def isBreakable(self, i: int) -> bool:
        if i >= len(self.s):
            return True
        
        if i not in self.memo:     
            for i0 in range(i, len(self.s)):
                if self.s[i:i0 + 1] in self.words and self.isBreakable(i0 + 1):
                    self.memo[i] = True
                    return True
            self.memo[i] = False
        
        return self.memo[i]
        
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.s = s
        self.words = wordDict
        return self.isBreakable(0)
