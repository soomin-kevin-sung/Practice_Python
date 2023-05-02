import java.util.*;

class Solution {
    public int[] solution(int[] arr, int[] query) {
        int start = 0, end = arr.length - 1;

        for (int i = 0; i < query.length; i++) {
            int idx = query[i];
            
            // even
            if (i % 2 == 0)
                end = start + idx;
            // odd
            else
                start += idx;
        }

        return Arrays.copyOfRange(arr, start, end + 1);
    }
}