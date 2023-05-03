class Solution {
    public int solution(String binomial) {
        String[] pkts = binomial.split(" [+\\-*] ");
        int a = Integer.parseInt(pkts[0]);
        int b = Integer.parseInt(pkts[1]);
        
        if (binomial.contains("+"))
            return a + b;
        else if (binomial.contains("-"))
            return a - b;
        else
            return a * b;
    }
}