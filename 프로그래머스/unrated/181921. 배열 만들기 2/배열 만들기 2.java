import java.util.ArrayList;

class Solution {
    public int[] solution(int l, int r) {
        ArrayList<Integer> result = new ArrayList<Integer>();
        
        while (l <= r) {
            if (isValid(l))
                result.add(l);
            
            l++;
        }
        
        if (result.size() > 0)
            return toArray(result);
        else
            return new int[] {-1};
    }
    
    private boolean isValid(int num) {
        String s = String.valueOf(num);
        int len = s.length();
        
        for (int i = 0; i < len; i++)
        {
            char c = s.charAt(i);
            if (c != '5' && c != '0')
                return false;
        }
        
        return true;
    }
    
    private int[] toArray(ArrayList<Integer> list) {
        int len = list.size();
        int[] answer = new int[len];
        for (int i = 0; i < len; i++)
            answer[i] = list.get(i).intValue();
        
        return answer;
    }
}