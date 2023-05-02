class Solution {
    public int solution(int a, int b) {
        StringBuilder builder = new StringBuilder();
        builder.append(a).append(b);
        
        return Math.max(Integer.parseInt(builder.toString()), 2 * a * b);
    }
}