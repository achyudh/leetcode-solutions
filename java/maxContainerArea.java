class Solution {
    public int maxArea(int[] height) {
        int lo = 0, hi = height.length - 1, maxArea = 0;
        
        while (lo < hi) {
            int currentArea = Math.min(height[lo], height[hi]) * (hi - lo);
            maxArea = Math.max(maxArea, currentArea);
            if (height[lo] < height[hi])
                lo++;
            else 
                hi--;
        }
        
        return maxArea;
    }
}
