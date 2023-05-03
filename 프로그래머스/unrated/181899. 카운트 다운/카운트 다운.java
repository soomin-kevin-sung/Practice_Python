import java.util.stream.*;

class Solution {
    public int[] solution(int start, int end) {
        return IntStream.iterate(start, i -> i - 1).limit(start - end + 1).toArray();
    }
}