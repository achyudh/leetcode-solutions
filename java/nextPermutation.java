class Solution {
    public void reverse(int[] nums, int start) {
        int temp, end = nums.length - 1;
        while (start < end) {
            temp = nums[start];
            nums[start] = nums[end];
            nums[end] = temp;
            start++;
            end--;
        }
    }
    
    public void nextPermutation(int[] nums) {
        if (nums.length < 2)
            return;
        
        // Find start of the exhausted sequence
        int start = nums.length - 2;
        while(start >= 0 && nums[start] >= nums[start + 1])
            start--;
        
        if (start >= 0) {       
            // Find the next consecutive element to swap
            int next = nums.length - 1;
            while (next > start && nums[next] <= nums[start])
                next--;
            
            // Swap with the next largest element
            int temp = nums[start];
            nums[start] = nums[next];
            nums[next] = temp;
        }
        
        // Reverse the exhausted sequence to get the next permutation
        reverse(nums, start + 1);
    }
}
