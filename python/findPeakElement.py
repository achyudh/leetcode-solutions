class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start_ptr = 0
        end_ptr = len(nums) - 1
        nums.append(float('-inf'))
        while start_ptr <= end_ptr:
            mid_ptr = (start_ptr + end_ptr) // 2
            if nums[mid_ptr - 1] < nums[mid_ptr]:
                if nums[mid_ptr + 1] < nums[mid_ptr]:
                    return mid_ptr
                else:
                    start_ptr = mid_ptr + 1
            else:
                end_ptr = mid_ptr - 1
        return 0y
