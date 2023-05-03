import java.util.*;

class Solution {
    public int[] solution(int[] arr, boolean[] flag) {
        Stack<Integer> st = new Stack();
        for (int i = 0; i < arr.length; i++) {
            if (flag[i])
                push(st, arr[i], arr[i] * 2);
            else
                pop(st, arr[i]);
        }
        
        int[] answer = new int[st.size()];
        for (int i = 0; i < answer.length; i++)
            answer[i] = st.get(i);
        
        return answer;
    }
    
    private void push(Stack<Integer> st, int v, int e) {
        for (int i = 0; i < e; i++)
            st.push(v);
    }
    
    private void pop(Stack<Integer> st, int e) {
        for (int i = 0; i < e && st.size() > 0; i++)
            st.pop();
    }
}