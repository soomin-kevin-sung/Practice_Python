import java.util.*;

class Solution {
    public int solution(int[] array) {
        Map<Integer, Integer> map = new HashMap<>();
        
        int answer = 0, max = 0;
        for (int i = 0; i < array.length; i++) {
            int value = map.getOrDefault(array[i], 0) + 1;
            if (max < value)
            {
                answer = array[i];
                max = value;
            }
            else if (max == value) {
                answer = -1;
            }
                
            map.put(array[i], value);
        }
        
        return answer;
    }
}