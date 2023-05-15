import java.util.*;

class Solution {
    public int[] solution(String[] keymap, String[] targets) {
        Map<Character, Integer> map = new HashMap<>();
        for (String s : keymap) {
            int len = s.length();
            for (int i = 0; i < len; i++) {
                char c = s.charAt(i);
                int v = map.getOrDefault(c, 101);
                map.put(c, Math.min(v, i + 1));
            }
        }
        
        int[] answer = new int[targets.length];
        for (int i = 0; i < answer.length; i++) {
            String target = targets[i];
            
            for (char c : target.toCharArray())
            {
                if (!map.containsKey(c)) {
                    answer[i] = -1;
                    break;
                }
                
                answer[i] += map.get(c);
            }
        }
        
        return answer;
    }
}