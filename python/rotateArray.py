class Solution:
    def rotate(self, nums: 'List[int]', k: 'int') -> 'None':
        """
        Do not return anything, modify nums in-place instead.
        """
        start_ptr = -1
        num_swaps = 0
        k = k % len(nums)
        
        while num_swaps < len(nums):
            start_ptr += 1
            curr_val = nums[start_ptr]
            next_ptr = (start_ptr + k) % len(nums)
            while next_ptr != start_ptr:
                temp_val = nums[next_ptr]
                nums[next_ptr] = curr_val
                num_swaps += 1
                curr_val = temp_val
                next_ptr = (next_ptr + k) % len(nums)
            temp_val = nums[next_ptr]
            nums[next_ptr] = curr_val
            num_swaps += 1
