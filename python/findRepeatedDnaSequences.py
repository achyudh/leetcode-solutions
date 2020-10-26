BASE_N = 4
SEQ_LENGTH = 10
MSB_MULTIPLIER = BASE_N ** 9
NUC_INT_MAP = {
    'A': 0, 'G': 1, 'C': 2, 'T': 3
}

def seqToBaseN(s: str) -> int:
    result = 0
    for nuc in s:
        result *= BASE_N
        result += NUC_INT_MAP[nuc]
    return result
    
class Solution:    
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        previousSequences = set()
        repeatedSequences = set()
        
        currentSeqRepr = seqToBaseN(s[:SEQ_LENGTH])
        previousSequences.add(currentSeqRepr)
        
        for seqEndPtr in range(SEQ_LENGTH, len(s)):
            currentSeqRepr -= MSB_MULTIPLIER * NUC_INT_MAP[s[seqEndPtr - SEQ_LENGTH]]
            currentSeqRepr *= BASE_N
            currentSeqRepr += NUC_INT_MAP[s[seqEndPtr]]
            
            if currentSeqRepr in previousSequences and currentSeqRepr not in repeatedSequences:
                repeatedSequences.add(s[seqEndPtr - SEQ_LENGTH + 1: seqEndPtr + 1])
            previousSequences.add(currentSeqRepr)
        
        return repeatedSequences

