import java.util.*;

class Solution {
    public String[] solution(String[] str_list) {
        List<String> list = Arrays.<String>asList(str_list);
        int l_idx = list.indexOf("l");
        int r_idx = list.indexOf("r");
        
        if (l_idx == -1 && r_idx == -1)
            return new String[0];
        else if (l_idx == -1)
            return Arrays.copyOfRange(str_list, r_idx + 1, str_list.length);
        else if (r_idx == -1)
            return Arrays.copyOfRange(str_list, 0, l_idx);
        else if (l_idx < r_idx)
            return Arrays.copyOfRange(str_list, 0, l_idx);
        else
            return Arrays.copyOfRange(str_list, r_idx + 1, str_list.length);
    }
}