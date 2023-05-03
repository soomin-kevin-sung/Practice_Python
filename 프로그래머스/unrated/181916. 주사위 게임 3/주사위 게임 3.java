import java.util.*;

class Solution {
    public int solution(int a, int b, int c, int d) {
        // a == b == c == d
        if (a == b && b == c && c == d)
            return 1111 * a;
        // a == b == c | d
        else if (a == b && b == c)
            return (int)Math.pow(10 * a + d, 2);
        // a == b == d | c
        else if (a == b && b == d)
            return (int)Math.pow(10 * a + c, 2);
        // a == c == d | b
        else if (a == c && c == d)
            return (int)Math.pow(10 * a + b, 2);
        // b == c == d | a
        else if (b == c && c == d)
            return (int)Math.pow(10 * b + a, 2);
        // a == b | c == d
        else if (a == b && c == d)
            return (a + c) * Math.abs(a - c);
        // a == c | b == d
        else if (a == c && b == d)
            return (a + b) * Math.abs(a - b);
        // a == d | b == c
        else if (a == d && b == c)
            return (a + b) * Math.abs(a - b);
        // a == b | c | d
        else if (a == b)
            return c * d;
        // a == c | b | d
        else if (a == c)
            return b * d;
        // a == d | b | c
        else if (a == d)
            return b * c;
        // b == c | a | d
        else if (b == c)
            return a * d;
        // b == d | a | c
        else if (b == d)
            return a * c;
        // c == d | a | b
        else if (c == d)
            return a * b;
        // a | b | c | d
        else
            return Math.min(a, Math.min(b, Math.min(c, d)));
    }
}