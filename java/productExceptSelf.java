class Solution {
    public int[] productExceptSelf(int[] nums) {
        
        int[] products = new int[nums.length];
        int[] rightProds = new int[nums.length];
            
        products[0] = 1;
        rightProds[nums.length - 1] = 1;

        for (int i = nums.length - 2; i >= 0; i--)
            rightProds[i] = rightProds[i + 1] * nums[i + 1];
        
        for (int i = 1; i < nums.length; i++)
            products[i] = products[i - 1] * nums[i - 1];
        
        for (int i = 0; i < nums.length; i++)
            products[i] = products[i] * rightProds[i];
        
        return products;
    }
}
