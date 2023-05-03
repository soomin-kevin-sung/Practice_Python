class Solution {
    public int[] solution(String my_string) {
        int len = my_string.length();
        int[] answer = new int[52];
        
        for (int i = 0; i < len; i++) {
            char c = my_string.charAt(i);
            if (Character.isLowerCase(c))
                answer[26 + (int)c - 97] += 1;
            else
                answer[(int)c - 65] += 1;
        }
        
        return answer;
    }
}