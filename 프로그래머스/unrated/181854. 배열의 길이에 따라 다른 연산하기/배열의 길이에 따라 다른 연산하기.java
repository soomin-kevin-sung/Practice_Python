class Solution {
    public int[] solution(int[] arr, int n) {
        int len = arr.length;
        int[] answer = new int[len];
        
        for (int i = 0; i < len; i++)
        {
            if (len % 2 != i % 2)
                answer[i] = arr[i] + n;
            else
                answer[i] = arr[i];
        }
        
        return answer;
    }
}