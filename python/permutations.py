class Solution:
    def __init__(self):
        self.permutations = list()
        
    def getPermutations(self, cstr):
        if len(self.nums) == len(cstr):
            self.permutations.append(cstr)
        else:
            for num in self.nums:
                if num not in cstr:
                    self.getPermutations((num,) + cstr)
                
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.nums = nums
        self.getPermutations(tuple())
        return self.permutations
