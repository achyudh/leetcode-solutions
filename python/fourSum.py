from collections import defaultdict

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # Cache all possible paired sums 
        pairSums = defaultdict(list)
        for i0 in range(len(nums)):
            for j0 in range(i0 + 1, len(nums)):
                pairSums[nums[i0] + nums[j0]].append((i0, j0))
        
        # Find distinct quadruplets from pairSums
        solution = set()
        for i0 in range(len(nums)):
            for j0 in range(i0 + 1, len(nums)):
                remainingSum = target - nums[i0] - nums[j0]
                for pair in pairSums[remainingSum]:
                    if i0 < pair[0] and j0 < pair[0]:
                        solution.add(tuple(sorted([nums[i0], nums[j0], 
                                                  nums[pair[0]], nums[pair[1]]])))

        return solution
