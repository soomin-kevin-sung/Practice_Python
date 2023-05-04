class Solution {
    public int solution(String myString, String pat) {
        myString = convert(myString);
        return myString.contains(pat) ? 1 : 0;
    }
    
    private String convert(String myString) {
        StringBuilder builder = new StringBuilder();
        int len = myString.length();
        
        for (int i = 0; i < len; i++) {
            char c = myString.charAt(i);
            if (c == 'A')
                builder.append('B');
            else
                builder.append('A');
        }
            
        
        return builder.toString();
    }
}