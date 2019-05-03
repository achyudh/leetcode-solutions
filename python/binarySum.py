class Solution:
    def __init__(self):
        self.mask = 0xFFFFFFFF
        self.max = 0x7FFFFFFF
    def getSum(self, a: 'int', b: 'int') -> 'int':
        if b == 0:
            return a if a <= self.max else ~(a ^ self.mask)
        else:
            return self.getSum((a ^ b) & self.mask, ((a & b) << 1) & self.mask)
      
