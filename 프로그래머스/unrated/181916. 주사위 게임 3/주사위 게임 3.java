import java.util.*;

class Solution {
    public int solution(int a, int b, int c, int d) {
        // a == b == c == d
        if (a == b && b == c && c == d)
            return ps1(a);
        // a == b == c | d
        else if (a == b && b == c)
            return ps2(a, d);
        // a == b == d | c
        else if (a == b && b == d)
            return ps2(a, c);
        // a == c == d | b
        else if (a == c && c == d)
            return ps2(a, b);
        // b == c == d | a
        else if (b == c && c == d)
            return ps2(b, a);
        // a == b | c == d
        else if (a == b && c == d)
            return ps3(a, c);
        // a == c | b == d
        else if (a == c && b == d)
            return ps3(a, b);
        // a == d | b == c
        else if (a == d && b == c)
            return ps3(a, b);
        // a == b | c | d
        else if (a == b)
            return ps4(c, d);
        // a == c | b | d
        else if (a == c)
            return ps4(b, d);
        // a == d | b | c
        else if (a == d)
            return ps4(b, c);
        // b == c | a | d
        else if (b == c)
            return ps4(a, d);
        // b == d | a | c
        else if (b == d)
            return ps4(a, c);
        // c == d | a | b
        else if (c == d)
            return ps4(a, b);
        // a | b | c | d
        else
            return ps5(a, b, c, d);
    }
    
    private int ps1(int a) {
        return 1111 * a;
    }
    
    private int ps2(int a, int b)
    {
        return (int)Math.pow(10 * a + b, 2);
    }
    
    private int ps3(int a, int b) {
        return (a + b) * Math.abs(a - b);
    }
    
    private int ps4(int a, int b) {
        return a * b;
    }
    
    private int ps5(int a, int b, int c, int d) {
        return Math.min(a, Math.min(b, Math.min(c, d)));
    }
}