class Solution {
    public boolean canJump(int[] nums) {
        int lastPos = nums.length - 1;
        for (int i0 = nums.length - 1; i0 >= 0; i0--)
            if (i0 + nums[i0] >= lastPos)
                lastPos = i0;
        return lastPos == 0;
    }
}
