import java.util.*;

class Solution {
    public int solution(int[][] board) {
        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[i].length; j++) {
                if (board[i][j] == 1)
                    setZone(board, i, j);
            }
        }
        
        int answer = board.length * board.length;
        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[i].length; j++) {
                if (board[i][j] > 0)
                    answer--;
            }
        }
        
        return answer;
    }
    
    private void setZone(int[][] board, int x, int y) {
        int[] dx = {0, 1, 1, 1, 0, -1, -1, -1};
        int[] dy = {1, 1, 0, -1, -1, -1, 0, 1};

        for (int i = 0; i < 8; i++) {
            int next_x = x + dx[i];
            int next_y = y + dy[i];
            
            if (0 <= next_x && next_x < board.length &&
                0 <= next_y && next_y < board[next_x].length && board[next_x][next_y] == 0)
                board[next_x][next_y] = 2;
        }
    }
}