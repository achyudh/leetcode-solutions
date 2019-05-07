class Solution {
    public int eraseOverlapIntervals(int[][] intervals) {
        if (intervals.length == 0)
            return 0;
        
        Arrays.sort(intervals, (o1, o2) -> Integer.compare(o1[1], o2[1]));
        
        int[] result = new int[2];
        result = intervals[0];
        int numOverlaps = 0;
        
        for (int i0 = 1; i0 < intervals.length; i0++) {
            if (intervals[i0][0] < result[1])
                numOverlaps += 1;
            else 
                result = intervals[i0];
        }
        
        return numOverlaps;
    }
}
