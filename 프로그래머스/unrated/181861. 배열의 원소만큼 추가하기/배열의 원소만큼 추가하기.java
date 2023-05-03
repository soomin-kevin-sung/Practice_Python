import java.util.*;

class Solution {
    public int[] solution(int[] arr) {
        ArrayList<Integer> list = new ArrayList();
        for (int e : arr)
        {
            for (int i = 0; i < e; i++)
                list.add(e);
        }
        
        return toArray(list);
    }
    
    private int[] toArray(List<Integer> list) {
        int[] answer = new int[list.size()];
        for (int i = 0; i < answer.length; i++)
            answer[i] = list.get(i);
        
        return answer;
    }
}