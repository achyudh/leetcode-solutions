class Task implements Comparable<Task> {
    public int name;
    public int order;
    public int lastExec;
    
    public Task(int name, int order, int lastExec) {
        this.name = name;
        this.order = order;
        this.lastExec = lastExec;
    }
    
    @Override
    public int compareTo(Task other) {
        return Integer.compare(this.order, other.order);
    }
}

class Solution {
    public int leastInterval(char[] tasks, int n) {
        int currTime = 0, tasksCompleted = 0;
        Task[] taskArray = new Task[26];
        int[] counts = new int[26];
        
        for (int i0 = 0; i0 < tasks.length; i0++)
            counts[tasks[i0] - 'A']++;
        
        for (int i0 = 0; i0 < 26; i0++)
            taskArray[i0] = new Task(i0, counts[i0], -n);
        
        while(tasksCompleted < tasks.length) {
            currTime++;
            Arrays.sort(taskArray);        
            for (int i0 = 25; i0 >= 0; i0--)
                if (taskArray[i0].order > 0 && 
                    taskArray[i0].lastExec + n < currTime) {
                        taskArray[i0].lastExec = currTime;
                        taskArray[i0].order--;
                        tasksCompleted++;
                        break;
                }
        }
        
        return currTime;
        
    }
}
