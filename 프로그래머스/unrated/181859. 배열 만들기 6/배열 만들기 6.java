import java.util.*;

class Solution {
    public int[] solution(int[] arr) {
        Stack<Integer> st = new Stack();
        int len = arr.length;
        
        for (int i = 0; i < len; i++) {
            if (!st.isEmpty() && st.peek() == arr[i])
                st.pop();
            else
                st.push(arr[i]);
        }
        
        return st.isEmpty() ? new int[] { -1 } : st.stream().mapToInt(e -> e).toArray();
    }
}