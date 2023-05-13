class Solution {
    public long solution(int r1, int r2) {
        long answer = 0;
        for (int i = 1; i <= r2; i++) {
            long start = (long)Math.ceil(getY(r1, i));
            long end = (long)Math.floor(getY(r2, i));
            
            answer += end - start + 1;
        }

        return answer * 4;
    }

    private double getY(long r, long x) {
        return Math.sqrt(r * r - x * x);
    }    
}