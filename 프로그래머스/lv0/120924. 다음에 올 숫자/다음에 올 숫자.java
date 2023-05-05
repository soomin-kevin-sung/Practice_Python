class Solution {
    public int solution(int[] common) {
        int n = common.length;
        int d0 = common[1] - common[0];
        int d1 = common[2] - common[1];
        
        if (d0 == d1)
            return common[n - 1] + d0;
        
        return common[n - 1] * (common[1] / common[0]);
    }
}