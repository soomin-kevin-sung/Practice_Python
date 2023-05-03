class Solution {
    public int solution(String myString, String pat) {
        int answer = 0;
        int idx = 0;
        while (true)
        {
            idx = myString.indexOf(pat, idx);
            if (idx == -1)
                break;
            
            idx++;
            answer++;
        }
        
        return answer;
    }
}