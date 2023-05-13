import java.util.*;

class Solution {
    public int solution(int[][] targets) {
        Arrays.sort(targets, (a, b) -> a[0] == b[0] ? b[1] - a[1] : a[0] - b[0]);
        
        int answer = 0, s = targets[0][0], e = targets[0][1];
        
        for (int i = 1; i < targets.length; i++) {
            if (targets[i][0] < e) {
                e = Math.min(e, targets[i][1]);
            }
            else {
                answer++;
                e = targets[i][1];
            }
            s = targets[i][0];
        }
        
        return answer + 1;
    }
}