import java.util.ArrayList;
public class Q29 {
    public ArrayList<Integer> printMatrix(int [][] matrix) {

        ArrayList<Integer> res = new ArrayList<>();
        if (matrix == null || matrix.length == 0) return res;

        int x=0, y=0;
        int m=matrix.length, n=matrix[0].length;
        int boundry=0;
        while (true){
            while (y<n-boundry){
                res.add(matrix[x][y]);
                y++;
            }
            y--; x++;
            if (res.size() == m*n) break;

            while (x<m-boundry){
                res.add(matrix[x][y]);
                x++;
            }
            x--; y--;
            if (res.size() == m*n) break;

            while (y>=boundry){
                res.add(matrix[x][y]);
                y--;
            }
            y++; x--;
            if (res.size() == m*n) break;

            boundry++;
            while (x>=boundry){
                res.add(matrix[x][y]);
                x--;
            }
            x++; y++;
            if (res.size() == m*n) break;
        }
        return res;
    }
}
