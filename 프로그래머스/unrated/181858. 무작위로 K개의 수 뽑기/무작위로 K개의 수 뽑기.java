class Solution {
    public int[] solution(int[] arr, int k) {
        boolean[] chk = new boolean[100001];
        int len = arr.length;
        int[] answer = new int[k];
        int cnt = 0;
        
        for (int i = 0; i < len && cnt < k; i++) {
            if (!chk[arr[i]])
                answer[cnt++] = arr[i];
            chk[arr[i]] = true;
        }
        
        while (cnt < k)
            answer[cnt++] = -1;
        
        return answer;
    }
}