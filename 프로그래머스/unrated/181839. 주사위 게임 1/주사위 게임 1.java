class Solution {
    public int solution(int a, int b) {
        boolean is_a_odd = a % 2 == 1;
        boolean is_b_odd = b % 2 == 1;
        
        if (is_a_odd && is_b_odd)
            return a * a + b * b;
        else if (!is_a_odd && !is_b_odd)
            return Math.abs(a - b);
        else
            return 2 * (a + b);
    }
}