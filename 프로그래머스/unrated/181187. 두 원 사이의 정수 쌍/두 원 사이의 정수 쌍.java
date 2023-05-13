class Solution {
    public long solution(int r1, int r2) {
        long answer = 0;
        int x = 1;
        while (x < r2) {
            double y1 = Math.ceil(x <= r1 ? getY(r1, x) : 0);
            double y2 = Math.floor(getY(r2, x));
            long n = (long)(y2 - y1) + 1;
            if (y1 == 0)
                n--;

            answer += n;
            x++;
        }
        
        return (answer + (r2 - r1 + 1)) * 4;
    }
    
    private double getY(long r, long x) {
        return Math.sqrt(r * r - x * x);
    }
}