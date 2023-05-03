import java.util.*;

class Solution {
    public int[] solution(int[] arr) {
        ArrayList<Integer> list = new ArrayList();
        int i = 0;
        
        while (i < arr.length) {
            if (!list.isEmpty() && list.get(list.size() - 1) == arr[i]) {
                list.remove(list.size() - 1);
                i++;
            }
            else {
                list.add(arr[i++]);
            }     
        }
        
        return list.isEmpty() ? new int[] { -1 } : list.stream().mapToInt(e -> e).toArray();
    }
}