class Solution {
    public int solution(int bridge_length, int weight, int[] truck_weights) {        
        int moving_weight = truck_weights[0];
        int head = 0, tail = 0, cnt = 0;
        int[] time = new int[truck_weights.length];
        
        moving_weight = truck_weights[tail];
        time[tail] = cnt;
        tail++;
        cnt++;
        
        while (head < tail) {
            if (head < time.length &&
                cnt - time[head] >= bridge_length) {
                moving_weight -= truck_weights[head];
                head++;
            }
            
            if (tail < truck_weights.length &&
                tail - head < bridge_length && 
                moving_weight + truck_weights[tail] <= weight)
            {
                moving_weight += truck_weights[tail];
                time[tail] = cnt;
                tail++;
            }
            
            cnt++;
        }
        
        return cnt;
    }
}