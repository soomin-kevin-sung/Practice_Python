import java.util.*;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        ArrayList<Integer> list = new ArrayList<>();
        int[] days = getDays(progresses, speeds);
        int max = 0, cnt = 0;
        for (int i = 0; i < days.length; i++) {
            if (max < days[i]) {
                if (cnt > 0)
                    list.add(cnt);
                
                cnt = 0;
                max = days[i];
            }
            
            cnt++;
        }
        
        if (cnt > 0)
            list.add(cnt);
        
        int[] answer = new int[list.size()];
        for (int i = 0; i < answer.length; i++)
            answer[i] = list.get(i);
        
        return answer;
    }
    
    private int[] getDays(int[] progresses, int[] speeds) {
        int[] answer = new int[progresses.length];
        for (int i = 0; i < answer.length; i++) {
            int left = 100 - progresses[i];
            if (left % speeds[i] == 0)
                answer[i] = (100 - progresses[i]) / speeds[i];
            else
                answer[i] = (100 - progresses[i]) / speeds[i] + 1;
        }
        
        return answer;
    }
}