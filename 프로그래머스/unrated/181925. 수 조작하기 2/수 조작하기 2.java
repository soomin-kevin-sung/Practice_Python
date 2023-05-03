class Solution {
    public String solution(int[] numLog) {
        StringBuilder builder = new StringBuilder();
        
        for (int i = 1; i < numLog.length; i++)
        {
            int k = numLog[i] - numLog[i - 1];
            switch (k) {
                case 1:
                    builder.append('w');
                    break;
                case -1:
                    builder.append('s');
                    break;
                case 10:
                    builder.append('d');
                    break;
                case -10:
                    builder.append('a');
                    break;
            }
        }
        
        return builder.toString();
    }
}