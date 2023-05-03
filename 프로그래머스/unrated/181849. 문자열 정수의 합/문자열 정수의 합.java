class Solution {
    public int solution(String num_str) {
        String[] pkts = num_str.split("");
        int sum = 0;
        
        for (String pkt : pkts)
            sum += Integer.valueOf(pkt);
        
        return sum;
    }
}