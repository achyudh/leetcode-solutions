class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        total = n * (n + 1) / 2
        
        for i0 in nums:
            total -= i0
        
        return total
