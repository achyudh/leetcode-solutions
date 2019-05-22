from collections import defaultdict

class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        num_pairs = 0
        sums_ab = defaultdict(list)
        sums_cd = defaultdict(list)
        
        for i in range(0, len(A)):
            for j in range(0, len(B)):
                sums_ab[A[i] + B[j]].append((i, j))
                
        for i in range(0, len(C)):
            for j in range(0, len(D)):
                sums_cd[C[i] + D[j]].append((i, j))
        
        for sum_ab, pairs_ab in sums_ab.items():
            if len(sums_cd[-sum_ab]) > 0:
                num_pairs += len(pairs_ab) * len(sums_cd[-sum_ab])
                
        return num_pairs
