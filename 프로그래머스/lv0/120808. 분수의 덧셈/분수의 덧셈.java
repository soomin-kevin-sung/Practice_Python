class Solution {
    public int[] solution(int numer1, int denom1, int numer2, int denom2) {
        int[] answer = new int[] { numer1 * denom2 + numer2 * denom1, denom1 * denom2 };
        
        int d = gcd(answer[1], answer[0]);
        answer[0] /= d;
        answer[1] /= d;
        
        return answer;
    }
    
    private int gcd(int a, int b) {
        if (a % b == 0)
            return b;
        
        return gcd(b, a % b);
    }
}