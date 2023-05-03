class Solution {
    public String solution(int q, int r, String code) {
        int lenOfCode = code.length();
        StringBuilder builder = new StringBuilder();
        
        for (int i = 0; i < lenOfCode; i++) {
            if (i % q == r)
                builder.append(code.charAt(i));
        }
        
        return builder.toString();
    }
}