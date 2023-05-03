import java.util.Arrays;

class Solution {
    public int solution(int[] rank, boolean[] attendance) {
        int numOfDatas = rank.length;
        Data[] datas = new Data[numOfDatas];
        for (int i = 0; i < numOfDatas; i++)
            datas[i] = new Data(i, rank[i], attendance[i]);
        
        Arrays.sort(datas);
        for (int i = 0; i < numOfDatas; i++)
            System.out.printf("%d ", datas[i].idx);
        
        return datas[0].idx * 10000 + datas[1].idx * 100 + datas[2].idx;
    }
    
    class Data implements Comparable<Data> {
        int idx;
        int rank;
        boolean attendance;
        
        public Data(int idx, int rank, boolean attendance) {
            this.idx = idx;
            this.rank = rank;
            this.attendance = attendance;
        }
        
        @Override
        public int compareTo(Data data) {
            if (this.attendance && data.attendance)
            {
                if (this.rank < data.rank)
                    return -1;
                else if (this.rank > data.rank)
                    return 1;
                else
                    return 0;
            }
            else if (this.attendance)
                return -1;
            else if (data.attendance)
                return 1;
            
            return 0;
        }
    }
}