class Solution {
    ArrayList<ArrayList<Integer>> graph;
    int[] visited;
    
    public boolean topoSort(int current) {
        visited[current] = 1;
        
        for (int next : graph.get(current))
            if (visited[next] == 1 || !topoSort(next))
                return false;
        
        visited[current] = 2;
        return true;
    }
    
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        graph = new ArrayList<>();
        visited = new int[numCourses];
        
        for (int i = 0; i < numCourses; i++)
            graph.add(new ArrayList<>());
        
        for (int[] prereq : prerequisites)
            graph.get(prereq[0]).add(prereq[1]);
        
        for (int start = 0; start < numCourses; start++)
            if (visited[start] != 2 && !topoSort(start))
                return false;
        
        return true;
    }
}
