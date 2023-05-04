class Solution {
    public int[] solution(int[] num_list, int n) {
        int len = num_list.length / n + (num_list.length % n > 0 ? 1 : 0);
        int[] answer = new int[len];
        int cnt = 0;
        
        for (int i = 0; i < num_list.length; i += n)
            answer[cnt++] = num_list[i];
        
        return answer;
    }
}