class Interval {
    public int start;
    public int end;
    public Interval(int start, int end) {
        this.start = start;
        this.end = end;
    }
}

class Solution {
    public int[][] merge(int[][] intervalArray) {
        ArrayList<Interval> intervals = new ArrayList<>();
        Arrays.sort(intervalArray, new Comparator<int[]>(){
            @Override
            public int compare(int[] a, int[] b){
                return a[0] - b[0];
            }
        });
        
        for (int[] interval : intervalArray) {
            if (!intervals.isEmpty() && 
                interval[0] <= intervals.get(intervals.size() - 1).end) {
                if (interval[1] > intervals.get(intervals.size() - 1).end)
                    intervals.get(intervals.size() - 1).end = interval[1];
            }
            else {
                intervals.add(new Interval(interval[0], interval[1]));
            }
        }
        
        int[][] returnArray = new int[intervals.size()][2];
        
        for (int i0 = 0; i0 < intervals.size(); i0++) {
            returnArray[i0][0] = intervals.get(i0).start;
            returnArray[i0][1] = intervals.get(i0).end;
        }
        
        return returnArray;
    }
}
