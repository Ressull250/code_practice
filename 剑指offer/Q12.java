public class Q12 {

    public boolean hasPath(char[] matrix, int rows, int cols, char[] str) {

        if (str.length == 0) return false;

        boolean[][] visit = new boolean[rows][cols];

        for (int i=0; i<rows; i++){
            for (int j=0; j<cols; j++){
                if (check(matrix, rows, cols, i, j, str, 0, visit))
                    return true;
            }
        }
        return false;
    }

    public static boolean check(char[] matrix, int rows, int cols, int x, int y, char[] str, int offset, boolean[][] visit){

        int off = cols*x + y;
        if (offset == str.length) return true;
        if (x>=0 && x<rows && y>=0 && y<cols && matrix[off] == str[offset] && !visit[x][y]){
            visit[x][y] = true;
            boolean result = check(matrix, rows, cols, x-1, y, str, offset+1, visit)
                    || check(matrix, rows, cols, x, y-1, str, offset+1, visit)
                    || check(matrix, rows, cols, x, y+1, str, offset+1, visit)
                    || check(matrix, rows, cols, x+1, y, str, offset+1, visit);
            visit[x][y] = false;
            return result;
        }
        return false;
    }
}
