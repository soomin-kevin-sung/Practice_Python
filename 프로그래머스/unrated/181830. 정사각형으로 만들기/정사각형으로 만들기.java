class Solution {
    public int[][] solution(int[][] arr) {
        int lenOfrows = arr.length;
        int lenOfcols = arr[0].length;
        int maxLen = Math.max(lenOfrows, lenOfcols);
        
        int[][] answer = new int[maxLen][maxLen];
        for (int i = 0; i < lenOfrows; i++) {
            for (int j = 0; j < lenOfcols; j++)
                answer[i][j] = arr[i][j];
        }
        
        return answer;
    }
}