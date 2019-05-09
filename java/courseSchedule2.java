class Solution {
    LinkedList<Integer> topoOrder;
    ArrayList<ArrayList<Integer>> graph;
    int[] visited;
    
    public boolean topoSort(int current) {
        visited[current] = 1;
        
        for (int next : graph.get(current))
            if (visited[next] == 1)
                return false;
            else if (visited[next] == 0 && !topoSort(next))
                return false;
        
        visited[current] = 2;
        topoOrder.add(current);
        return true;
    }
    
    public int[] findOrder(int numCourses, int[][] prerequisites) {
        visited = new int[numCourses];
        graph = new ArrayList<>();
        topoOrder = new LinkedList<>();
        
        for (int i = 0; i < numCourses; i++)
            graph.add(new ArrayList<>());
        
        for (int[] prereq : prerequisites)
            graph.get(prereq[0]).add(prereq[1]);

        for (int i = 0; i < numCourses; i++)
            if (visited[i] == 0 && !topoSort(i))
                return new int[0];
        
        int j = 0;
        int[] result = new int[numCourses];
        for (int i : topoOrder)
            result[j++] = i;
        
        return result;
    }
}
