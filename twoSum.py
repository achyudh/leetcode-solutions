class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        arr_map = dict()
        for i0 in range(len(nums)):
            arr_map[nums[i0]] = i0
        for i0 in range(len(nums)):
            if target - nums[i0] in arr_map.keys() and arr_map[target - nums[i0]] != i0:
                return i0, arr_map[target - nums[i0]] 
