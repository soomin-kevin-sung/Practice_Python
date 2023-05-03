class Solution {
    public String solution(String my_string, int m, int c) {
        StringBuilder builder = new StringBuilder();
        int len = my_string.length();
        
        for (int i = 0; i < len; i += m) {
            if (i + c - 1 < len)
                builder.append(my_string.charAt(i + c - 1));
        }
        
        return builder.toString();
    }
}