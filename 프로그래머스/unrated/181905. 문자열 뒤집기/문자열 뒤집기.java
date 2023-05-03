class Solution {
    public String solution(String my_string, int s, int e) {
        StringBuilder builder = new StringBuilder(my_string);
        StringBuilder reverseBuilder = new StringBuilder(builder.substring(s, e + 1));
        builder.replace(s, e + 1, reverseBuilder.reverse().toString());
        return builder.toString();
    }
}