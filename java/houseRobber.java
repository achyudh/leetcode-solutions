class Solution {
    int[] nums;
    int[][] memo;
    
    public int maxMoney(int index, boolean canRob) {
        if (index >= nums.length)
            return 0;
        
        else if (memo[index][canRob ? 1 : 0] == -1) {
            if (canRob)
                memo[index][1] = Math.max(maxMoney(index + 1, true), maxMoney(index + 1, false) + nums[index]);
            else 
                memo[index][0] = maxMoney(index + 1, true);                
        }
        
        return memo[index][canRob ? 1 : 0];
    }
    
    public int rob(int[] nums) {
        this.nums = nums;
        this.memo = new int[nums.length][2];
        for (int i = 0; i < nums.length; i++) {
            this.memo[i][0] = -1;
            this.memo[i][1] = -1;            
        }
        
        return maxMoney(0, true);
    }
}
