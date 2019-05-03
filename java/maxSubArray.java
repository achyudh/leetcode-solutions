class Solution {
    public int maxSubArray(int[] nums) {
        int maxSum = nums[0];
        int currSum = nums[0];
        int currIter = 1;
        
        while (currIter < nums.length) {
            currSum = currSum + nums[currIter];
            
            if (nums[currIter] >= currSum)
                currSum = nums[currIter];
            
            if (currSum > maxSum) 
                maxSum = currSum;
            
            currIter++;
        }
        
        return maxSum;
    }
}
