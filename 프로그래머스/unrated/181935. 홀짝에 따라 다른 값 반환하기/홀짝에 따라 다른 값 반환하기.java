class Solution {
    public int solution(int n) {
        int answer = 0;
        
        int c = 0;
        while (c <= n) {
            if (c % 2 == n % 2)
                answer += c % 2 == 1 ? c : c * c;
            
            c++;
        }
        
        return answer;
    }
}