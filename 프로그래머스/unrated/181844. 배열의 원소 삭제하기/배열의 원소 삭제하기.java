import java.util.*;

class Solution {
    public int[] solution(int[] arr, int[] delete_list) {
        boolean[] chks = getCheckArray(delete_list);
        ArrayList<Integer> list = new ArrayList();
        
        for (int e : arr) {
            if (!chks[e])
                list.add(e);
        }
        
        return toArray(list);
    }
    
    private boolean[] getCheckArray(int[] delete_list) {
        boolean[] chks = new boolean[1001];
        for (int e : delete_list)
            chks[e] = true;
        
        return chks;
    }
    
    private int[] toArray(List<Integer> list) {
        int[] answer = new int[list.size()];
        for (int i = 0; i < answer.length; i++)
            answer[i] = list.get(i);
        
        return answer;
    }
}