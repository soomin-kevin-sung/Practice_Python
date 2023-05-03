class Solution {
    public String[] solution(String[] picture, int k) {
        int len = picture.length;
        String[] answer = new String[len * k];
        
        for (int i = 0; i < len; i++)
        {
            String[] row = picture[i].split("");
            
            StringBuilder builder = new StringBuilder();   
            for (String col : row)
                builder.append(col.repeat(k));
            
            for (int j = 0; j < k; j++)
                answer[i * k + j] = builder.toString();
        }
        
        return answer;
    }
}