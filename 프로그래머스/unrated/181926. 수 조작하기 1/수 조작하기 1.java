class Solution {
    public int solution(int n, String control) {
        int len = control.length();
        for (int i = 0; i < len; i++) {
            switch (control.charAt(i))
            {
                case 'w':
                    n++;
                    break;
                case 's':
                    n--;
                    break;
                case 'd':
                    n += 10;
                    break;
                case 'a':
                    n -= 10;
                    break;
            }
        }
        
        return n;
    }
}