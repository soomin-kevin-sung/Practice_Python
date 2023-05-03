import java.util.*;

class Solution {
    public int[] solution(int[] arr) {
        Stack<Integer> st = new Stack();
        int i = 0;
        
        while (i < arr.length) {
            if (!st.isEmpty() && st.peek() >= arr[i])
                st.pop();
            else
                st.push(arr[i++]);
        }
        
        return st.stream().mapToInt(e -> e).toArray();
    }
}