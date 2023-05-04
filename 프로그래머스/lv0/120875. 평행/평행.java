class Solution {
    public int solution(int[][] dots) {
        if (getSlope(dots[0], dots[1]) == getSlope(dots[2], dots[3]) ||
            getSlope(dots[0], dots[2]) == getSlope(dots[1], dots[3]) ||
            getSlope(dots[0], dots[3]) == getSlope(dots[1], dots[2]))
            return 1;
        
        return 0;
    }
    
    private double getSlope(int[] p1, int[] p2) {
        return (double)(p1[1] - p2[1]) / (p1[0] - p2[0]);
    }
}