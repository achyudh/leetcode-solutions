class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = nums[0]
        curr_sum = nums[0]
        for i0 in range(1, len(nums)):
            if nums[i0] > curr_sum + nums[i0]:
                curr_sum = nums[i0]
            else:
                curr_sum = curr_sum + nums[i0]
            if curr_sum > max_sum:
                max_sum = curr_sum
        return max_sum
