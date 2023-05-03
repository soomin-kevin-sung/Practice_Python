class Solution {
    public String solution(String myString) {
        int len = myString.length();
        StringBuilder builder = new StringBuilder();
        for (int i = 0; i < len; i++) {
            char c = Character.toLowerCase(myString.charAt(i));
            if (c == 'a')
                builder.append('A');
            else
                builder.append(c);
        }
        
        return builder.toString();
    }
}