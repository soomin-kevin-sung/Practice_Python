import java.util.Arrays;

class Solution {
    public int[] solution(int[] arr) {
        int len = arr.length;
        int s = indexOf(arr, 2);
        int e = lastIndexOf(arr, 2);
        
        if (s == -1)
            return new int[] { -1 };
        else
            return Arrays.copyOfRange(arr, s, e + 1);
    }
    
    private int indexOf(int[] arr, int e) {
        for (int i = 0 ; i < arr.length; i++) {
            if (arr[i] == e)
                return i;
        }
        
        return -1;
    }
    
    private int lastIndexOf(int[] arr, int e) {
        for (int i = arr.length - 1; i >= 0; i--) {
            if (arr[i] == e)
                return i;
        }
        
        return -1;
    }
}