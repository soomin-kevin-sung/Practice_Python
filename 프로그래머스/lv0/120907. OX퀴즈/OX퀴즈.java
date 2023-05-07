class Solution {
    public String[] solution(String[] quiz) {
        String[] answer = new String[quiz.length];
        
        for (int i = 0; i < quiz.length; i++) {
            String[] pkts = quiz[i].split(" = ");
            String[] exp = pkts[0].split(" [+-] ");
            int a = Integer.parseInt(exp[0]);
            int b = Integer.parseInt(exp[1]);
            int x = Integer.parseInt(pkts[1]);
            
            if (pkts[0].contains("+"))
                answer[i] = a + b == x ? "O" : "X";
            else
                answer[i] = a - b == x ? "O" : "X";
        }
        
        return answer;
    }
}