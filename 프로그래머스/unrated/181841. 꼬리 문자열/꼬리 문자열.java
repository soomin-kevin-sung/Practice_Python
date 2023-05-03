class Solution {
    public String solution(String[] str_list, String ex) {
        StringBuilder builder = new StringBuilder();
        for (String s : str_list) {
            if (!s.contains(ex))
                builder.append(s);
        }
        
        return builder.toString();
    }
}