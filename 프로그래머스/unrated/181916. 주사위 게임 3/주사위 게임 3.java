import java.util.*;

class Solution {
    public int solution(int a, int b, int c, int d) {
        Map<Integer, Integer> map = new HashMap<Integer, Integer>();
        countScore(map, a);
        countScore(map, b);
        countScore(map, c);
        countScore(map, d);
        
        int[] keys = map.keySet().stream().mapToInt(Integer::intValue).toArray();
        switch (keys.length) {
            case 1:
                return 1111 * a;
                
            case 2:
                if (map.get(keys[0]) == 3)
                    return (int)Math.pow(10 * keys[0] + keys[1], 2);
                else if (map.get(keys[1]) == 3)
                    return (int)Math.pow(10 * keys[1] + keys[0], 2);
                else
                    return (keys[0] + keys[1]) * Math.abs(keys[0] - keys[1]);
                    
            case 3:
                if (map.get(keys[0]) == 2)
                    return keys[1] * keys[2];
                else if (map.get(keys[1]) == 2)
                    return keys[0] * keys[2];
                else
                    return keys[0] * keys[1];
                    
                
            case 4:
                return Math.min(a, Math.min(b, Math.min(c, d)));
        }
        
        return -1;
    }
    
    private void countScore(Map<Integer, Integer> map, Integer key) {
        Integer old = map.getOrDefault(key, Integer.valueOf(0));
        
        map.put(key, old + 1);
    }
}