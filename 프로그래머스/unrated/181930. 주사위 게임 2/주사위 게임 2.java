class Solution {
    public int solution(int a, int b, int c) {
        int answer = 0;
        if (a == b && b == c)
            return (a + b + c) *
                (power(a, 2) + power(b, 2) + power(c, 2)) *
                (power(a, 3) + power(b, 3) + power(c, 3));
        else if (a == b || a == c || b == c)
            return (a + b + c) * (power(a, 2) + power(b, 2) + power(c, 2));
        else
            return a + b + c;
    }
    
    private int power(int a, int b) {
        return (int)Math.pow(a, b);
    }
}