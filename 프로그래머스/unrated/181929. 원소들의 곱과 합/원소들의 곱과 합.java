import java.util.stream.*;

class Solution {
    public int solution(int[] num_list) {
        IntStream st = IntStream.of(num_list);
        int sum = IntStream.of(num_list).sum();
        int mul = IntStream.of(num_list).reduce(1, (x, y) -> x * y);
        
        return mul < sum * sum ? 1 : 0;
    }
}