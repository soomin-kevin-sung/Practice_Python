class Solution {
    public int[] solution(int numer1, int denom1, int numer2, int denom2) {
        int[] answer = new int[] { numer1 * denom2 + numer2 * denom1, denom1 * denom2 };
        
        boolean flag = true;
        while (flag) {
            flag = false;
            for (int i = 2; i <= 1000 && !flag; i++)
            {
                if (answer[0] % i == 0 && answer[1] % i == 0)
                {
                    answer[0] /= i;
                    answer[1] /= i;
                    flag = true;
                }
            }            
        }
        
        return answer;
    }
}