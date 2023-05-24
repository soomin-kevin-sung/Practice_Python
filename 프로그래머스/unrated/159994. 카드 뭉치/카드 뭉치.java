import java.util.*;

class Solution {
    public String solution(String[] cards1, String[] cards2, String[] goal) {        
        int[] idx = { 0, 0 };
        for (int i = 0; i < goal.length; i++) {
            if (idx[0] < cards1.length && cards1[idx[0]].equals(goal[i]))
                idx[0]++;
            else if (idx[1] < cards2.length && cards2[idx[1]].equals(goal[i]))
                idx[1]++;
            else
                return "No";
        }
        
        return "Yes";
    }
}