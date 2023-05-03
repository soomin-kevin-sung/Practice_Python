class Solution {
    public int[] solution(int[] arr, int[][] queries) {
        int[] answer = new int[queries.length];
        
        for (int i = 0; i < queries.length; i++)
            answer[i] = findMin(arr, queries[i]);
        
        return answer;
    }
    
    private int findMin(int[] arr, int[] query) {
        int answer = -1;
        for (int i = query[0]; i <= query[1]; i++)
        {
            if (arr[i] > query[2] && (arr[i] < answer || answer == -1))
                answer = arr[i];
        }
        
        return answer;
    }
}