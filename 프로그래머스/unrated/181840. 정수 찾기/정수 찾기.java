class Solution {
    public int solution(int[] num_list, int n) {
        int numOfList = num_list.length;
        for (int i = 0; i < numOfList; i++)
        {
            if (num_list[i] == n)
                return 1;
        }
        
        return 0;
    }
}