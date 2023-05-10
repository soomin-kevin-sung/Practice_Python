import java.util.*;

class Solution {
    public int solution(int bridge_length, int weight, int[] truck_weights) {        
        TruckQueue q = new TruckQueue(bridge_length, weight, truck_weights);
        int time = 0;
        
        q.push(time);
        time++;
        
        while (q.isTruckLeft()) {
            if (q.canPop(time))
                q.pop();
            
            if (q.canPush())
                q.push(time);
            
            time++;
        }
        
        return time;
    }
    
    private class TruckQueue {   
        public TruckQueue(int bridge_length, int weight, int[] truck_weights) {
            this.bridge_length = bridge_length;
            this.weight = weight;
            this.truck_weights = truck_weights;
            this.time = new int[truck_weights.length];
        }
        
        int bridge_length;
        int weight;
        int[] truck_weights;
        int[] time;
        int head;
        int tail;
        int moving_weight;
        int date;
        
        public boolean isTruckLeft() {
            return head < tail;
        }
        
        public boolean canPush() {
            return tail < truck_weights.length &&
                tail - head < bridge_length && 
                moving_weight + truck_weights[tail] <= weight;
        }
        
        public void push(int t) {
            moving_weight += truck_weights[tail];
            time[tail] = t;
            tail++;
        }
        
        public boolean canPop(int t) {
            return head < time.length &&
                t - time[head] >= bridge_length;
        }
        
        public void pop() {
            moving_weight -= truck_weights[head];
            head++;
        }
    }
}