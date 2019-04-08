class Solution:
    def __init__(self):
        self.combinations = list()
        self.mapping = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        
    def enumerateCombinations(self, cpos, cstr):
        if cpos == len(self.digits):
            self.combinations.append(cstr)
        else:
            for letter in self.mapping[self.digits[cpos]]:
                self.enumerateCombinations(cpos + 1, cstr + letter)
                
    def letterCombinations(self, digits: str) -> List[str]:
        if digits != "":
            self.digits = digits
            self.enumerateCombinations(0, '')
        return self.combinations
