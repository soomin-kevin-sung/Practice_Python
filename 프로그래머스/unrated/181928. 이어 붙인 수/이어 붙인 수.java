class Solution {
    public int solution(int[] num_list) {
        StringBuilder evenBuilder = new StringBuilder();
        StringBuilder oddBuilder = new StringBuilder();
        
        for (int i = 0; i < num_list.length; i++) {
            if (num_list[i] % 2 == 0)
                evenBuilder.append(num_list[i]);
            else
                oddBuilder.append(num_list[i]);
        }
        
        return Integer.parseInt(evenBuilder.toString()) + Integer.parseInt(oddBuilder.toString());
    }
}