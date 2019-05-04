from collections import defaultdict

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = defaultdict(int)
        for task in tasks:
            counts[task] += 1
        
        taskOrder = [[v, k, -n] for k, v in counts.items()]
        tasksCompleted = 0
        currentTime = 0
        
        while tasksCompleted < len(tasks):
            currentTime += 1
            taskOrder = sorted(taskOrder, reverse=True)
            for i0 in range(len(taskOrder)):
                if taskOrder[i0][0] and taskOrder[i0][2] + n < currentTime:
                    tasksCompleted += 1
                    taskOrder[i0][0] -= 1
                    taskOrder[i0][2] = currentTime
                    break
                    
        return currentTime
