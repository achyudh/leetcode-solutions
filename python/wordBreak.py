class Solution:
    def __init__(self):
        self.memo = dict()
        
    def isBreakable(self, lo: int, hi: int) -> bool:
        if lo >= hi:
            return True
        
        if (lo, hi) not in self.memo:     
            for i0 in range(lo, hi):
                if self.s[lo:i0 + 1] in self.words and self.isBreakable(i0 + 1, hi):
                    self.memo[(lo, hi)] = True
                    return True
            self.memo[(lo, hi)] = False
        
        return self.memo[(lo, hi)]
        
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.s = s
        self.words = wordDict
        return self.isBreakable(0, len(s))
