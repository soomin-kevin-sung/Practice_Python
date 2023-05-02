class Solution {
    public int solution(int a, int b) {
        String a_string = String.valueOf(a);
        String b_string = String.valueOf(b);
        int ab = Integer.parseInt(a_string + b_string);
        
        return Math.max(ab, 2 * a * b);
    }
}