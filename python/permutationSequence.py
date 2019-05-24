class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        permutation = []
        factorials = [1]
        choices = [x for x in range(1, n + 1)]
        
        k -= 1
        for i0 in range(1, n + 1):
            factorials.append(factorials[-1] * i0)
        
        while choices:
            index = k // factorials[len(choices) - 1]
            k -= index * factorials[len(choices) - 1]
            permutation.append(choices.pop(index))
                               
        return ''.join(str(x) for x in permutation)
