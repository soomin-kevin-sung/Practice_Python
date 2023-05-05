import java.util.*;

class Solution {
    public String solution(String[] participant, String[] completion) {
        Map<String, Integer> map = new HashMap();
        for (String e : participant)
            map.put(e, map.getOrDefault(e, 0) + 1);
            
        
        for (String e : completion)
            map.put(e, map.getOrDefault(e, 0) - 1);
        
        for (String e : map.keySet()) {
            if (map.get(e) > 0)
                return e;
        }
        
        return "";
    }
}