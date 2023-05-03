class Solution {
    public int solution(String num_str) {
        int lenOfString = num_str.length();
        int sum = 0;
        
        for (int i = 0; i < lenOfString; i++) {
            sum += Integer.valueOf(num_str.charAt(i) - 48).intValue();
        }
        
        return sum;
    }
}