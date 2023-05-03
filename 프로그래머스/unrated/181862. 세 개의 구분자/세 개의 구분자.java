import java.util.*;
class Solution {
    public String[] solution(String myStr) {
        ArrayList<String> list = new ArrayList<String>(Arrays.asList(myStr.split("a")));
        list = getSplitStrings(list, "b");
        list = getSplitStrings(list, "c");
        
        if (list.size() == 0)
            return new String[] { "EMPTY" };
        else
            return list.toArray(new String[0]);
    }
    
    private ArrayList<String> getSplitStrings(ArrayList<String> strings, String splitter) {
        ArrayList<String> list = new ArrayList();
        for (String s : strings) {
            for (String pkt : s.split(splitter))
            {
                if (!pkt.isEmpty())
                    list.add(pkt);
            }
        }
        
        return list;
    }
}