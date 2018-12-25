public class Q13 {

    public int movingCount(int threshold, int rows, int cols) {
        if (rows == 0) return 0;
        boolean visited[][] = new boolean[rows][cols];

        return helper(threshold, visited, rows, cols, 0, 0);
    }

    int helper(int threshold, boolean[][] visited, int rows, int cols, int x, int y){
        if (x>=0 && x<rows && y>=0 && y<cols && !visited[x][y] && count(x)+count(y) <= threshold){
            visited[x][y] = true;
            return 1
                    + helper(threshold, visited, rows, cols, x-1, y)
                    + helper(threshold, visited, rows, cols, x, y-1)
                    + helper(threshold, visited, rows, cols, x+1, y)
                    + helper(threshold, visited, rows, cols, x, y+1);
        }
        return 0;
    }

    int count(int rows){
        int c = 0;
        while (rows != 0){
            c += rows % 10;
            rows /= 10;
        }
        return c;
    }
}
