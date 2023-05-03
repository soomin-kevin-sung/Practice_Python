class Solution {
    public String solution(String code) {
        StringBuilder builder = new StringBuilder();
        int mode = 0;
        int idx = 0;
        int len = code.length();
        
        while (idx < len) {
            char chr = code.charAt(idx);
            if (chr == '1')
                mode += 1;
            else if (idx % 2 == mode % 2)
                builder.append(chr);
            
            idx++;
        }
        
        if (builder.length() == 0)
            return "EMPTY";
        else
            return builder.toString();
    }
}