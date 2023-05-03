class Solution {
    public int solution(String[] strArr) {
        int[] cnts = new int[31];
        int maxCnt = 0;
        for (String str : strArr) {
            int len = str.length();
            cnts[len]++;
            maxCnt = Math.max(maxCnt, cnts[len]);
        }

        return maxCnt;
    }
}