import java.util.Arrays;

class Solution {
    public int solution(int[] arr) {
        int answer = 0;
        int[] prevArr = arr;
        while (true) {
            answer++;
            int[] newArr = getCalculatedArray(prevArr);
            if (Arrays.equals(prevArr, newArr))
                return answer - 1;
            
            prevArr = newArr;
        }
    }
    
    private int[] getCalculatedArray(int[] arr) {
        int[] answer = new int[arr.length];
        
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] >= 50 && arr[i] % 2 == 0)
                answer[i] = arr[i] / 2;
            else if (arr[i] < 50 && arr[i] % 2 == 1)
                answer[i] = arr[i] * 2 + 1;
            else
                answer[i] = arr[i];
        }
        
        return answer;
    }
}