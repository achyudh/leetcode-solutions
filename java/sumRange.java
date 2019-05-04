/**
 * Usage for NumArray:
 * NumArray obj = new NumArray(nums);
 * int param_1 = obj.sumRange(i,j);
 */
 
class NumArray {
    private int[] prefixSum;

    public NumArray(int[] nums) {
        prefixSum = new int[nums.length + 1];  
        int currSum = 0, ctr = 0;
        
        for (int num : nums) {
            prefixSum[ctr++] = currSum;
            currSum += num;
        }
        
        prefixSum[ctr] = currSum;
    }
    
    public int sumRange(int i, int j) {
        return prefixSum[j + 1] - prefixSum[i];
    }
}
