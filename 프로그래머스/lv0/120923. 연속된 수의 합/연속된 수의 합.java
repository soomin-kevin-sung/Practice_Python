class Solution {
    public int[] solution(int num, int total) {
        int n = (int)(((2 * total) / num - num + 1) / 2);
        int[] answer = new int[num];
        for (int i = 0; i < num; i++)
            answer[i] = i + n;
        
        return answer;
    }
}