class Solution:
    def moveZeroes(self, nums: 'List[int]') -> 'None':
        """
        Do not return anything, modify nums in-place instead.
        """
        pos_ptr = 0
        for i0 in range(len(nums)):
            print(nums)
            if nums[i0] != 0:
                nums[pos_ptr], nums[i0] = nums[i0], nums[pos_ptr]
                pos_ptr += 1
