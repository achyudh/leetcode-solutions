from collections import defaultdict
from heapq import nsmallest

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counts = defaultdict(int)
        
        for word in words:
            counts[word] += 1
        
        return [x[0] for x in nsmallest(k, counts.items(), key=lambda x: (-x[1], x[0]))]            
        
