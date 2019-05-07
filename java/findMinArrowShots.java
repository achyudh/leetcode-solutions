class Solution {
    public int findMinArrowShots(int[][] points) {
        Arrays.sort(points, (o1, o2) -> Integer.compare(o1[1], o2[1]));
        if (points.length == 0) 
            return 0;
        
        int[] currentRange = points[0];
        int minArrows = 0;
        
        for (int i = 1; i < points.length; i++) {
            if (points[i][0] <= currentRange[1]) {
                currentRange[0] = Math.max(points[i][0], currentRange[0]);
                currentRange[1] = Math.min(points[i][1], currentRange[1]);
            }
            else {
                minArrows += 1;
                currentRange = points[i];
            }
        }

    return minArrows + 1;
    }
}
