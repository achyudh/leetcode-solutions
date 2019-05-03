class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 0:
            return -1, -1
        
        ptr_u = len(nums) - 1
        ptr_l = 0
        while ptr_u >= ptr_l:
            ptr_m = (ptr_u + ptr_l) // 2
            if nums[ptr_m] <= target:
                ptr_l = ptr_m + 1
            else:
                ptr_u = ptr_m - 1
        
        ptr_a = ptr_l - 1
        if nums[ptr_a] != target:
            return -1, -1
        
        ptr_u = len(nums) - 1
        ptr_l = 0
        while ptr_u >= ptr_l:
            ptr_m = (ptr_u + ptr_l) // 2
            if nums[ptr_m] >= target:
                ptr_u = ptr_m - 1
            else:
                ptr_l = ptr_m + 1
        
        return ptr_l, ptr_a
