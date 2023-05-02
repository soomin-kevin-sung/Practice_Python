class Solution {
    public String solution(String str1, String str2) {
        int length = str1.length();
        StringBuilder builder = new StringBuilder();
        
        for (int i = 0; i < str1.length(); i++) {
            builder.append(str1.charAt(i));
            builder.append(str2.charAt(i));
        }
        
        return builder.toString();
    }
}