class Solution:
    def canJump(self, nums: 'List[int]') -> 'bool':
        lr_node = len(nums) - 1
        for i0 in range(len(nums) - 2, -1, -1):
            if i0 + nums[i0] >= lr_node:
                lr_node = i0
        return 0 == lr_node
