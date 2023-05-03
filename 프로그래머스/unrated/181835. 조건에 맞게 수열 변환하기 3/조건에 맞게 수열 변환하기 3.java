import java.util.stream.*;

class Solution {
    public int[] solution(int[] arr, int k) {
        IntStream arrStream = IntStream.of(arr);
        if (k % 2 == 0)
            return arrStream.map(t -> t + k).toArray();
        else
            return arrStream.map(t -> t * k).toArray();
    }
}