from collections import deque

class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        score = 0
        maxScore = 0
        headPtr = 0
        tailPtr = len(tokens) - 1
        tokens.sort()
        
        while headPtr <= tailPtr and (power >= tokens[headPtr] or score):
            while headPtr <= tailPtr and power >= tokens[headPtr]:
                score += 1
                power -= tokens[headPtr]
                headPtr += 1
                
            maxScore = max(score, maxScore)
                
            if headPtr <= tailPtr and score:
                score -= 1
                power += tokens[tailPtr]
                tailPtr -= 1

        return maxScore
  
