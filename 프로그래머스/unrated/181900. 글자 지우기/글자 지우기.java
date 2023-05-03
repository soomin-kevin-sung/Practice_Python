class Solution {
    public String solution(String my_string, int[] indices) {
        int len = my_string.length();
        boolean[] chks = getCheckArray(len, indices);
        
        StringBuilder builder = new StringBuilder();
        for (int i = 0; i < len; i++) {
            if (!chks[i])
                builder.append(my_string.charAt(i));
        }
        
        return builder.toString();
    }
    
    private boolean[] getCheckArray(int maxLength, int[] indices) {
        boolean[] chks = new boolean[maxLength];
        for (int i : indices)
            chks[i] = true;
        
        return chks;
    }
}