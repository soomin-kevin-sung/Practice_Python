import java.math.*;

class Solution {
    public String solution(String a, String b) {
        BigInteger big_a = new BigInteger(a);
        BigInteger big_b = new BigInteger(b);
        return big_a.add(big_b).toString();
    }
}