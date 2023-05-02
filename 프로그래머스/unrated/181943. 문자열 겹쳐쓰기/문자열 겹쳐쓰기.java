class Solution {
    public String solution(String my_string, String overwrite_string, int s) {
        StringBuilder builder = new StringBuilder();
        
        int idx = 0;
        var my_chrs = my_string.toCharArray();
        while (idx < s)
            builder.append(my_chrs[idx++]);
        
        var overwrite_chrs = overwrite_string.toCharArray();
        for (var c : overwrite_chrs)
            builder.append(c);
        
        idx = s + overwrite_chrs.length;
        while (idx < my_chrs.length)
            builder.append(my_chrs[idx++]);
        
        return builder.toString();
    }
}