import java.util.*;
class Solution {
    public String[] solution(String myStr) {
        ArrayList<String> list = new ArrayList();
        String[] pkts = myStr.split("[abc]+");
        for (String pkt : pkts)
        {
            if (!pkt.isEmpty())
                list.add(pkt);
        }
        
        return list.size() == 0 ? new String[] { "EMPTY" } : list.toArray(new String[0]);
    }
}