import java.util.*;

class Solution {
    public int[] solution(int[] num_list) {
        int[] answer = Arrays.copyOf(num_list, num_list.length + 1);
        int a = num_list[num_list.length - 1];
        int b = num_list[num_list.length - 2];
        
        if (a > b)
            answer[num_list.length] = a - b;
        else
            answer[num_list.length] = a * 2;
        
        return answer;
    }
}