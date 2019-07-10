class Solution:
    def __init__(self):
        self.combinations = list()
    
    def addCombinations(self, n: int, k: int, startIndex: int, combination: List[int]):
        if len(combination) == k:
            self.combinations.append(list(combination))
        else:
            for i in range(startIndex, n + 1):
                if i not in combination:
                    self.addCombinations(n, k, i, combination | {i})
    
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.addCombinations(n, k, 1, set())
        return self.combinations
