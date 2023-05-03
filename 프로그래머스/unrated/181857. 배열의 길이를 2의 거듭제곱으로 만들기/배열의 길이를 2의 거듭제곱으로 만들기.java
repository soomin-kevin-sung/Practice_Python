import java.util.*;

class Solution {
    public int[] solution(int[] arr) {
        int e = 0;
        while (Math.pow(2, e++) < arr.length);
        return Arrays.copyOf(arr, (int)Math.pow(2, e - 1));
    }
}