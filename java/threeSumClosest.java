class Solution {
    public int threeSumClosest(int[] nums, int target) {
        int closest = nums[0] + nums[1] + nums[2], current;
        Arrays.sort(nums);
        
        for(int i = 0; i < nums.length - 2; i++) {
            int target2 = target - i;
            int j = i + 1, k = nums.length - 1;
            
            while (j < k) {
                current = nums[i] + nums[j] + nums[k];
                if (Math.abs(target - current) < Math.abs(target- closest))
                    closest = current;    
                if (current > target)
                    k--;
                else
                    j++;
            }
        }
        
        return closest;
    }
}
