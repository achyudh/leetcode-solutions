class Solution:
    def partitionHelper(self, index: int, sumLeft: int) -> bool:
        if (index, sumLeft) not in self.memo:
            # Ran out of array elements
            if index == len(self.nums):
                result = False
            
            # Successful partition
            elif sumLeft == 0:
                result = True
                
            else:
                result = self.partitionHelper(index + 1, sumLeft) \
                    or self.partitionHelper(index + 1, sumLeft - self.nums[index])
            
            # Save the result to the memo
            self.memo[(index, sumLeft)] = result
        
        return self.memo[(index, sumLeft)]
        
    def canPartition(self, nums: List[int]) -> bool:
        self.nums = nums
        self.memo = dict()
        
        arraySum = sum(nums)
        if arraySum % 2:
            return False
        
        return self.partitionHelper(0, arraySum//2)
