class Solution {
    public String solution(String myString) {
        char[] answer = new char[myString.length()];
        for (int i = 0; i < answer.length; i++)
        {
            char c = myString.charAt(i);
            if (c < 'l')
                answer[i] = 'l';
            else
                answer[i] = c;
        }
        
        return new String(answer);
    }
}