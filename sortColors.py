class Solution(object):
    def partition(self, lo, hi, pivot):
        i0 = lo
        for i1 in range(lo, hi):
            if self.nums[i1] < pivot:
                self.nums[i0], self.nums[i1] = self.nums[i1], self.nums[i0]
                i0 += 1
        return i0
            
        
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        self.nums = nums
        if len(nums) > 1:
            p = self.partition(0, len(nums), 1)
            self.partition(p, len(nums), 2)
