class Solution {
    public int solution(String my_string, String is_suffix) {
        int len_myString = my_string.length();
        int len_suffix = is_suffix.length();
        
        if (len_myString >= len_suffix) {
            for (int i = 1; i <= len_suffix; i++)
            {
                if (my_string.charAt(len_myString - i) != is_suffix.charAt(len_suffix - i))
                    return 0;
            }
            
            return 1;
        }
            
        return 0;
    }
}