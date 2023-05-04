class Solution {
    public int solution(String my_string, String is_prefix) {
        if (my_string.length() < is_prefix.length())
            return 0;
        
        return my_string.indexOf(is_prefix) == 0 ? 1 : 0;
    }
}