class Solution {
    public int[][] solution(int n) {
        int[][] answer = new int[n][n];        
        int d = 0;
        int[] dx = new int[] { 0, 1, 0, -1 };
        int[] dy = new int[] { 1, 0, -1, 0 };        
        
        int x = 0, y = 0, num = 1;
        setNumber(answer, x, y, num++);
        
        while (num <= n * n) {
            int nextX = x + dx[d];
            int nextY = y + dy[d];
            
            if (isValidPos(answer, nextX, nextY)) {
                setNumber(answer, nextX, nextY, num++);
                x = nextX;
                y = nextY;
            }
            else {
                d = (d + 1) % 4;
            }
        }
        
        return answer;
    }
    
    private void setNumber(int[][] board, int x, int y, int num) {
        board[x][y] = num;
    }
    
    private boolean isValidPos(int[][] board, int x, int y) {
        int n = board.length;
        return x >= 0 && x < n && y >= 0 && y < n && board[x][y] == 0;
    }
}