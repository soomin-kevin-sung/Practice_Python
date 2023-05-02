import java.util.ArrayList;

class Solution {
    public int[] solution(int[] arr, int[] query) {
        int start = 0, end = arr.length;

        for (int i = 0; i < query.length; i++) {
            int idx = query[i];
            
            // even
            if (i % 2 == 0)
                end = start + idx;
            // odd
            else
                start += idx;
        }
        
        end = Math.min(end, arr.length - 1);
        var answer = new int[end - start + 1];
        for (int i = 0; i < answer.length; i++)
            answer[i] = arr[i + start];
        
        return answer;
    }
}