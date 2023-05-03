import java.util.*;

class Solution {
    public int[] solution(String[] intStrs, int k, int s, int l) {
        ArrayList<Integer> list = new ArrayList();
        for (String str : intStrs) {
            Integer v = Integer.parseInt(str.substring(s, s + l));
            if (v > k)
                list.add(v);
        }
            
        return toArray(list);
    }
    
    private int[] toArray(ArrayList<Integer> list) {
        int[] result = new int[list.size()];
        for (int i = 0; i < result.length; i++)
            result[i] = list.get(i);
        
        return result;
    }
}