import java.util.*;

class Solution {
    public int[] solution(String myString) {
        ArrayList<Integer> list = new ArrayList();
        int length = myString.length();
        int start = 0;
        
        for (int i = 0; i <= length; i++) {
            if (i == length || myString.charAt(i) == 'x') {
                list.add(i - start);
                start = i + 1;
            }
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