import java.util.*;

class Solution {
    public String solution(String[] cards1, String[] cards2, String[] goal) {
        Map<String, Integer> map = new HashMap<>();
        
        for (int i = 0; i < cards1.length; i++)
            map.put(cards1[i], (i + 1));
        
        for (int i = 0; i < cards2.length; i++)
            map.put(cards2[i], -(i + 1));
        
        int[] idx = { 0, 0 };
        for (int i = 0; i < goal.length; i++) {
            int v = map.get(goal[i]);
            if (v > 0 && v - idx[0] == 1)
                idx[0] = v;
            else if (v < 0 && idx[1] - v == 1)
                idx[1] = v;
            else
                return "No";
        }
        
        return "Yes";
    }
}