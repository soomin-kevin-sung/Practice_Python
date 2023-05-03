import java.util.*;

class Solution {
    public String[] solution(String my_string) {
        String[] answer = new String[my_string.length()];
        StringBuilder builder = new StringBuilder(my_string);
        
        for (int i = 0; i < answer.length; i++)
        {
            answer[i] = builder.toString();
            builder.deleteCharAt(0);
        }
        
        Arrays.sort(answer);
        return answer;
    }
}