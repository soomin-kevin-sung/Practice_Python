class Solution {
    public String solution(String my_string, int[][] queries) {
        StringBuilder builder = new StringBuilder(my_string);
        
        for (int[] query : queries)
            reverse(builder, query[0], query[1]);
        
        return builder.toString();
    }
    
    private void reverse(StringBuilder builder, int s, int e) {
        StringBuilder newBuilder = new StringBuilder(builder.substring(s, e + 1));
        newBuilder.reverse();
        builder.replace(s, e + 1, newBuilder.toString());
    }
}