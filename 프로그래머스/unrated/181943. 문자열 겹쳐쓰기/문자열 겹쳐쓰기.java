class Solution {
    public String solution(String my_string, String overwrite_string, int s) {
        var before = my_string.substring(0, s);
        var after = my_string.substring(s + overwrite_string.length());
        return before + overwrite_string + after;
    }
}