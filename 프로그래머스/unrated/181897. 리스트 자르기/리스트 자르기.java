import java.util.*;

class Solution {
    public int[] solution(int n, int[] slicer, int[] num_list) {
        switch (n) {
            case 1:
                return Arrays.copyOf(num_list, slicer[1] + 1);
            case 2:
                return Arrays.copyOfRange(num_list, slicer[0], num_list.length);
            case 3:
                return Arrays.copyOfRange(num_list, slicer[0], slicer[1] + 1);
            case 4:
                return getProcessedArray(num_list, slicer);
        }
        
        return null;
    }
    
    private int[] getProcessedArray(int[] num_list, int[] slicer) {
        List<Integer> list = new ArrayList();
        for (int i = slicer[0]; i <= slicer[1]; i += slicer[2])
            list.add(num_list[i]);
        
        int[] answer = new int[list.size()];
        for (int i = 0; i < answer.length; i++)
            answer[i] = list.get(i);
        
        return answer;
    }
}