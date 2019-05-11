class Solution {
    
    public boolean canJump(int[] nums) {
        for (int i0 = nums.length - 1; i0 > 0; i0--) {
            boolean isAcc = false;
            
            for (int i1 = i0 - 1; i1 >= 0; i1--)
                if (i1 + nums[i1] >= i0) {
                    isAcc = true;
                    break;
                }
            
            if (!isAcc) return false;
        }
        
        return true;
    }
}
