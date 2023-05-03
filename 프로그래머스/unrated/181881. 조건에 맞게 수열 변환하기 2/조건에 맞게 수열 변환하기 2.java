import java.util.Arrays;

class Solution {
    public int solution(int[] arr) {
        int answer = 0;
        for (int i = 0; i < arr.length; i++)
            answer = Math.max(answer, getMaxChangeCount(arr[i]));
        
        return answer;
    }
    
    private int getMaxChangeCount(int n) {
        int answer = 0;
        
        while (true) {
            if (n >= 50 && n % 2 == 0)
                n /= 2;
            else if (n < 50 && n % 2 == 1)
                n = n * 2 + 1;
            else
                break;
            answer++;
        }
        
        return answer;
    }
}