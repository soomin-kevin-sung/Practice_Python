import java.util.*;

class Solution {
    public int solution(int[] priorities, int location) {
        Queue<Process> q = getQueue(priorities);
        priorities = getSortedPriorities(priorities);        
        
        int step = 0;
        while (q.size() > 0) {
            Process e = q.poll();
            if (e.priority < priorities[step]) {
                q.add(e);
            }
            else {
                if (e.index == location)
                    return step + 1;
                
                step++;
            }
        }
        
        return 0;
    }
    
    private Queue<Process> getQueue(int[] priorities) {
        Queue<Process> q = new LinkedList();
        for (int i = 0; i < priorities.length; i++)
            q.add(new Process(i, priorities[i]));
        
        return q;
    }
    
    private int[] getSortedPriorities(int[] priorities) {
        Integer[] integers = new Integer[priorities.length];
        for (int i = 0; i < integers.length; i++)
            integers[i] = priorities[i];
        
        Arrays.sort(integers, Collections.reverseOrder());
        for (int i = 0; i < priorities.length; i++)
            priorities[i] = integers[i].intValue();
        
        return priorities;
    }
    
    class Process {
        public Process(int index, int priority) {
            this.index = index;
            this.priority = priority;
        }
        
        int index;
        int priority;
    }
}