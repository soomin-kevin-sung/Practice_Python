class Solution {
    public int solution(int[] num_list) {
        int answer = 0;
        for (int n : num_list)
            answer += getCalcCount(n);
        
        return answer;
    }
    
    private int getCalcCount(int n) {
        int cnt = 0;
        while (n > 1) {
            if (n % 2 == 0)
                n /= 2;
            else
                n = (n - 1) / 2;
            
            cnt++;
        }
        
        return cnt;
    }
}