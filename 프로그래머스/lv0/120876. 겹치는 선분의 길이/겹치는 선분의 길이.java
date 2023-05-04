class Solution {
    public int solution(int[][] lines) {
        int[] chk = new int[201];
        for (int[] line : lines)
        {
            for (int i = line[0]; i < line[1]; i++)
                chk[i + 100]++;
        }
        
        int answer = 0;
        for (int i = 0; i < chk.length; i++)
        {
            if (chk[i] > 1)
                answer++;
        }
        
        return answer;
    }
}