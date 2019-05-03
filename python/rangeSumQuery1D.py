class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.prefix_sums = [0]
        for num in nums:
            self.prefix_sums.append(num + self.prefix_sums[-1])    
        

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.prefix_sums[j+1] - self.prefix_sums[i]
