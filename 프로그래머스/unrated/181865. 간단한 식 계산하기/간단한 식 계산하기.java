class Solution {
    public int solution(String binomial) {
        String[] pkts = binomial.split(" ");
        int a = Integer.parseInt(pkts[0]);
        String op = pkts[1];
        int b = Integer.parseInt(pkts[2]);
        
        if (op.equals("+"))
            return a + b;
        else if (op.equals("-"))
            return a - b;
        else
            return a * b;
    }
}