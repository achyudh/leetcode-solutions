class Solution {
    public int[][] kClosest(int[][] points, int K) {
        PriorityQueue<int[]> heap = new PriorityQueue<>(
            (o1, o2) -> (o1[1] * o1[1] + o1[0] * o1[0]) - (o2[1] * o2[1] + o2[0] * o2[0])
        );
        
        for (int[] point : points)
            heap.add(point);
        
        int[][] result = new int[K][2];
        for (int i = 0; i < K; i++)
            result[i] = heap.poll();
        
        return result;
    }
}
