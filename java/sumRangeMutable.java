class NumArray {
    int[] nums, sums;
    int sqrtLen;

    public NumArray(int[] nums) {
        this.nums = nums;
        this.sqrtLen = (int) Math.ceil(nums.length / Math.sqrt(nums.length));
        this.sums = new int[sqrtLen];
        
        for (int i = 0; i < nums.length; i++) {
            sums[i/sqrtLen] += nums[i];
        }
    }
    
    public void update(int i, int val) {
        sums[i/sqrtLen] += (val - nums[i]);
        nums[i] = val;
    }
    
    public int sumRange(int i, int j) {
        int sqrtLo =  i / sqrtLen;
        int sqrtHi = j /sqrtLen;
        int sum = 0;
        
        if (sqrtLo == sqrtHi) {
            for (int k = i; k <= j; k++)
                sum += nums[k];
        }
        
        else {
            for (int k = sqrtLo + 1; k < sqrtHi; k++)
                sum += sums[k];

            for (int k = i; k < (sqrtLo + 1) * sqrtLen; k++)
                sum += nums[k];

            for (int k = sqrtHi * sqrtLen; k <= j; k++)
                sum += nums[k];
        }
        
        return sum;
    }
}

/**
 * Usage of NumArray object:
 * NumArray obj = new NumArray(nums);
 * obj.update(i,val);
 * int param_2 = obj.sumRange(i,j);
 */
