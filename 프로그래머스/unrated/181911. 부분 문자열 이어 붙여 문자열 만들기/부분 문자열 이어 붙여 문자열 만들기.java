class Solution {
    public String solution(String[] my_strings, int[][] parts) {
        StringBuilder builder = new StringBuilder();
        
        for (int i = 0; i < my_strings.length; i++)
            builder.append(my_strings[i].substring(parts[i][0], parts[i][1] + 1));
        
        return builder.toString();
    }
}