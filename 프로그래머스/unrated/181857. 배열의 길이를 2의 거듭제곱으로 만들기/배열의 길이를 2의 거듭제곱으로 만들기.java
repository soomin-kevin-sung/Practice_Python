import java.util.*;

class Solution {
    public int[] solution(int[] arr) {
        int len = arr.length;
        
        int e = -1;
        while (Math.pow(2, ++e) < len);
        
        return Arrays.copyOf(arr, (int)Math.pow(2, e));
    }
}