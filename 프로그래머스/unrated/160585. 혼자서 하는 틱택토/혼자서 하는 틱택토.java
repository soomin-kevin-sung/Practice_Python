class Solution {
    public int solution(String[] board) {
        int o = 0, x = 0;
        char[][] chars = getArray(board);
        int[] counts = getCount(chars);
        boolean[] lines = hasLine(chars);
        
        int c = counts[0] - counts[1];
        if ((c < 0 || c > 1) ||
            (lines[0] && lines[1]) ||
            (lines[0] && c != 1) ||
            (lines[1] && c != 0))
            return 0;
        
        return 1;
    }
    
    private char[][] getArray(String[] board) {
        char[][] chars = new char[3][0];
        
        for (int i = 0; i < 3; i++)
            chars[i] = board[i].toCharArray();
        
        return chars;
    }
    
    private int[] getCount(char[][] chars) {
        int o = 0, x = 0;
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                if (chars[i][j] == 'O')
                    o++;
                else if (chars[i][j] == 'X')
                    x++;
            }
        }
        
        return new int[] { o, x };
    }
    
    private boolean[] hasLine(char[][] chars) {
        boolean o = false, x = false;
        int[][][] idxes = {
            { {0, 0}, {0, 1}, {0, 2} },
            { {1, 0}, {1, 1}, {1, 2} },
            { {2, 0}, {2, 1}, {2, 2} },
            { {0, 0}, {1, 0}, {2, 0} },
            { {0, 1}, {1, 1}, {2, 1} },
            { {0, 2}, {1, 2}, {2, 2} },
            { {0, 0}, {1, 1}, {2, 2} },
            { {0, 2}, {1, 1}, {2, 0} }
        };
        
        for (int i = 0; i < idxes.length; i++) {
            int[][] idx = idxes[i];
            if (chars[idx[0][0]][idx[0][1]] == chars[idx[1][0]][idx[1][1]] &&
                chars[idx[1][0]][idx[1][1]] == chars[idx[2][0]][idx[2][1]]) {
                if (chars[idx[0][0]][idx[0][1]] == 'O')
                    o = true;
                else if (chars[idx[0][0]][idx[0][1]] == 'X')
                    x = true;
            }
        }
        
        return new boolean[] { o, x };
    }
}