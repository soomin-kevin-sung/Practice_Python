import java.math.*;

class Solution {
    public int solution(String number) {
        int len = number.length();
        int answer = 0;
        
        for (int i = 0; i < len; i++)
            answer = (answer + number.charAt(i) - 48) % 9;
        
        return answer;
    }
}