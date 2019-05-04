class Solution {
    public int maxProfit(int[] prices) {
        int maxProfit = 0;
        
        if (prices.length > 0) {
            int minPrice = prices[0];
            for (int i0 = 1; i0 < prices.length; i0++) {
                minPrice = Math.min(minPrice, prices[i0]);
                maxProfit = Math.max(maxProfit, prices[i0] - minPrice);
            }
        }   
        
        return maxProfit;
    }
}
