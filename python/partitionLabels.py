class Solution:
    def buildCharIndex(self):
        self.charIndex = [None for _ in range(len(self.s))]
        charIndexSet = set()
        
        for i0 in range(len(self.s) - 1, -1, -1):
            charIndexSet.add(self.s[i0])
            self.charIndex[i0] = charIndexSet.copy()
            
    def findPartitions(self):
        self.partitions = list()
        includedChars = set()
        lastPartitionIndex = 0
        
        for i0 in range(len(self.s) - 1):
            includedChars.add(self.s[i0])
            if not includedChars.intersection(self.charIndex[i0 + 1]):
                self.partitions.append(i0 - lastPartitionIndex + 1)
                lastPartitionIndex = i0 + 1
        self.partitions.append(len(self.s) - lastPartitionIndex)
        
        
    def partitionLabels(self, s: str) -> List[int]:
        self.s = s
        self.buildCharIndex()
        self.findPartitions()
        return self.partitions

