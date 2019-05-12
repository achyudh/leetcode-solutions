class Solution {
    int[] nums, memo;
    
    public int lengthOfLIS(int pos) {
        if (pos >= nums.length)
            return 0;
        
        if (memo[pos] == 0) {
            int maxSeqLen = 1;   
            for (int i = pos + 1; i < nums.length; i++)
                if (nums[i] > nums[pos])
                    maxSeqLen = Math.max(1 + lengthOfLIS(i), maxSeqLen);
            memo[pos] = maxSeqLen;
        }

        return memo[pos];
    }
    
    public int lengthOfLIS(int[] nums) {
        this.nums = nums;
        this.memo = new int[nums.length];
        int maxSeqLen = 0;
        for (int i = 0; i < nums.length; i++)
            maxSeqLen = Math.max(maxSeqLen, lengthOfLIS(i));
        return maxSeqLen;
    }
}
