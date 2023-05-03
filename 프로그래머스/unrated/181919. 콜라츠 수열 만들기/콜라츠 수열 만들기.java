import java.util.*;

class Solution {
    public int[] solution(int n) {
        ArrayList<Integer> list = new ArrayList();
        list.add(n);
        
        while (n > 1) {
            if (n % 2 == 0)
                n /= 2;
            else
                n = 3 * n + 1;
            
            list.add(n);
        }
        
        return toArray(list);
    }
    
    private int[] toArray(ArrayList<Integer> list) {
        int[] answer = new int[list.size()];
        for (int i = 0; i < answer.length; i++)
            answer[i] = list.get(i);
        
        return answer;
    }
}