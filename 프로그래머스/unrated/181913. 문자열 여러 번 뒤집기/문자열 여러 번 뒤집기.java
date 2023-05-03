class Solution {
    public String solution(String my_string, int[][] queries) {
        char[] chrs = my_string.toCharArray();
        
        for (int[] query : queries)
            reverse(chrs, query[0], query[1]);
        
        return new String(chrs);
    }
    
    private void reverse(char[] chrs, int s, int e) {
        int len = (s + e) / 2 - s;
        for (int i = 0; i <= len; i++) {
            char tmp = chrs[i + s];
            chrs[i + s] = chrs[e - i];
            chrs[e - i] = tmp;
        }
    }
}