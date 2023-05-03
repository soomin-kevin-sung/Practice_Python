import java.util.*;

class Solution {
    public int solution(int[] num_list) {
        if (num_list.length > 10)
            return Arrays.stream(num_list).reduce(0, Integer::sum);
        else
            return Arrays.stream(num_list).reduce(1, (x,y) -> x * y);
    }
}